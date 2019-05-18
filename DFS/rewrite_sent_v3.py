from py2neo import Graph, Node, Relationship, NodeMatcher
import re
import pymysql
from sqlalchemy import create_engine
import pandas as pd

test_graph = Graph('bolt://10.181.160.188:7687', user='neo4j', password='Abcd1234')
cat_cn = 'mysql+pymysql://charley:Abcd1234@10.123.4.222:3306/cat_angas?charset=utf8mb4'
cat_engine = create_engine(cat_cn)


def get_connection(host,user,password,database):
    connection = pymysql.connect(
        host = host,
        user = user,
        password = password,
        db = database,
        charset='UTF8MB4')
    return connection


def get_nodes(graph, entity="Subject"):
    node_names = graph.run("MATCH (n: %s) RETURN n.name AS nn" % entity).data()
    names = [name['nn'] for name in node_names]
    return names

node_labels = ['Subject', 'Action', 'Party', 'Descriptor', 'ActionDescriptor']
nodes = {label: get_nodes(test_graph, entity=label) for label in node_labels}
vocabs = []
for item in nodes.values():
    vocabs += item
vocabs = list(set(vocabs))


def get_relationship(graph, e1='Subject', n1='motion', e2='Action', n2='denied'):
    rel = graph.run("""MATCH (m: %s {name: "%s"})-[r]->(n: %s {name: "%s"}) RETURN type(r) as rel""" % (e1, n1, e2, n2)
                   ).data()
    if len(rel) == 1:
        return rel[0]['rel']
    elif len(rel) > 1:
        return [rel[i]['rel'] for i in range(len(rel))]
    else:
        return ''


def confused_labels(word, res):
    res_sent = " ".join(res)
    judgment_phrase = ['motion for summary judgment', 'motions for summary judgment',
                       'motion for judgment', 'motions for judgment',
                       'motion for a judgment',
                       'motion for partial summary judgment', 'motions for partial summary judgment']
    leave_phrase = ['motion for leave', 'motions for leave']
    remand_phrase = ['motion to remand', 'motions to remand']
    if word == 'judgment':
        ss = sum([1 if x in res_sent else 0 for x in judgment_phrase])
    elif word == 'leave':
        ss = sum([1 if x in res_sent else 0 for x in leave_phrase])
    else:
        ss = sum([1 if x in res_sent else 0 for x in remand_phrase])
    return 'Descriptor' if ss >= 1 else 'Subject'


def get_label(word, res):
    # res : list of words
    filters = ['judgment', 'leave', 'remand', 'case', 'order', 'claims']
    if word in nodes['Subject']:
        if word not in filters:
            return 'Subject'
        elif ('motion' not in res) and ('motions' not in res):
            return 'Subject'
        else:
            if word in filters[:3]:
                return confused_labels(word, res)
            else:
                return 'Descriptor'
    elif word in nodes['Action']:
        if word != 'recommended':
            return 'Action'
        else:
            return 'Recommended'
    elif word in nodes['Party']:
        return 'Party'
    elif word in nodes['Descriptor']:
        return 'Descriptor'
    else:
        return 'ActionDescriptor'


def is_valid(string, next_char):
    new_str = string + next_char
    # 'sas' in new_str or 'asa' in new_str or 'saas' in new_str or 'assa' in new_str:
    num = len(new_str)
    if num > 2:
        for i in range(1, num-1):
            substr1 = 's' + 'a' * i + 's'
            substr2 = 'a' + 's' * i + 'a'
            if (substr1 in new_str) or (substr2 in new_str):
                return False
        return True
    else:
        return True


def sent_split(sent):
    labels = []
    labels_id = []
    # print('origin sent: ', sent)
    for i, word in enumerate(sent):
        # label = get_label(word, sent[:i+1])
        label = get_label(word, sent)
        if label == 'Subject':
            labels.append('s')
            labels_id.append(i)
        elif label == 'Action':
            labels.append('a')
            labels_id.append(i)
    #label_count = Counter(labels)
    #print(labels, labels_id)

    ocs = []
    valid_oc = ''
    oc_ids = []
    while labels:
        next_char = labels.pop(0)
        next_id = labels_id.pop(0)
        if (not valid_oc) or is_valid(valid_oc, next_char):
            valid_oc += next_char
            oc_ids.append(next_id)
        else:
            ocs.append(oc_ids)
            valid_oc = next_char
            oc_ids = [next_id]
    ocs.append(oc_ids)
    return ocs


def get_subsent(ocs, sent):
    ocs_locations = []
    if len(ocs) == 1:
        ocs_locations.append( [0, len(sent)] )
        return ocs_locations
    for j in range(len(ocs)):
        beginning = 0 if j == 0 else ocs_locations[j-1][1]

        if j < len(ocs) - 1:
            second_sent_begin = ocs[j+1][0]
            if "'" in sent[second_sent_begin - 1]:
                if sent[second_sent_begin - 2] in nodes['Party']: # magistrate judge's
                    ocs_locations.append( [beginning, second_sent_begin - 2] )
                else:
                    ocs_locations.append( [beginning, second_sent_begin - 1] )
            else:
                w1 = sent[second_sent_begin - 1]
                w2 = sent[second_sent_begin]
                rel = get_relationship(test_graph, e1='Descriptor', n1=w1, e2='Subject', n2=w2)
                if rel == 'PHRASE':
                    if sent[second_sent_begin - 2] in nodes['Party']:
                        ocs_locations.append( [beginning, second_sent_begin - 1] )
                    else:
                        ocs_locations.append( [beginning, second_sent_begin - 1] )
                else:
                    ocs_locations.append( [beginning, second_sent_begin] )
        else: # last item
            ocs_locations.append( [beginning, len(sent)] )
    return ocs_locations


def check_sent(sent):
    words = sent.split()
    pop_ids = []
    nwords = len(words)
    for i, word in enumerate(words):
        if i+1 < len(words):
            if "'" in word:
                label_after = get_label(words[i+1], words)
                if label_after == "Action" or label_after == "ActionDescriptor":
                    pop_ids.append(i)
        else:
            label = get_label(word, words)
            if label != "Action" and label != "ActionDescriptor":
                pop_ids.append(i)
    pop_ids.reverse()

    for x in pop_ids:
        words.pop(x)
    return " ".join(words)


def coexist_items(sent):
    # sent : string
    if 'memorandum' in sent and 'memorandum and recommendation' not in sent:
        sent = re.sub(r"memorandum ", r" ", sent)
    if 'decision' in sent:
        decision_set = {'vacated', 'remanded', 'affirmed', 'reversed'}
        sent_set = set(sent.split())
        if not (decision_set & sent_set):
            sent = re.sub(r"decision ", r" ", sent)
    if 'issued' in sent:
        if ('report' not in sent) and ('recommendation' not in sent):
            sent = re.sub(r"issued ", r" ", sent)
    return sent


def rewrite_single_sent(sent):
    """sent : string"""
    sent = coexist_items(sent)
    sent = sent.split()
    ## split sent by syntax rules
    ocs = sent_split(sent)
    ## find accuracy "split_tag" location
    ocs_locations = get_subsent(ocs, sent)
    # print(ocs_locations)
    new_ocs = []
    for start, end in ocs_locations:
        ## get subsent
        subsent = sent[start:end]
        ## generate new sent
        sent_subject = []
        sent_action = []
        num_subject = 0
        num_action = 0
        new_sent = ''
        for i, word in enumerate(subsent):
            if word not in vocabs:
                continue
            # label = get_label(word, subsent[:i+1])
            label = get_label(word, subsent)
            if label == 'Subject':
                if num_subject == 0:
                    num_subject += 1
                else:
                    if subsent[i-1] == 'of':
                        sent_subject.append('of')
                    else:
                        label_before = get_label(sent_subject[-1], subsent)
                        if label_before != 'Party':
                            sent_subject.append('and')
                sent_subject.append(word)
            elif label == 'Party':
                if "'" in word or subsent[i+1] == "judge's":
                    sent_subject.append(word)
            elif label == 'Descriptor':
                if sent_subject:
                    label_before = get_label(sent_subject[-1], subsent[:i])
                    rel = get_relationship(test_graph, e1=label_before, n1=sent_subject[-1], e2='Descriptor', n2=word)
                    if rel == "PHRASE":
                        sent_subject.append(word)
                    elif rel:
                        sent_subject.append(rel.lower())
                        sent_subject.append(word)
                else:
                    if i+1 < len(subsent):
                        if (word == 'summary' and subsent[i+1] == 'judgment') or (word == 'claim' and subsent[i+1] == 'terms'):
                            sent_subject.append(word)
            elif label == 'Action':
                if num_action == 0:
                    num_action += 1
                else:
                    sent_action.append('and')
                sent_action.append(word)
            elif label == 'ActionDescriptor':
                if sent_action:
                    label_before = get_label(sent_action[-1], subsent[:i])
                    rel = get_relationship(test_graph, e1=label_before, n1=sent_action[-1], e2='ActionDescriptor', n2=word)
                    if isinstance(rel, str):
                        sent_action.append(rel.lower())
                        sent_action.append(word)
                    elif isinstance(rel, list) and subsent[i-1] in rel:
                        sent_action.append(subsent[i-1])
                        sent_action.append(word)
            else: # Recommended
                new_sent = 'recommended that '

        new_sent += " ".join(sent_subject + sent_action)
        # print(new_sent)
        new_sent = check_sent(new_sent)
        if is_sent_2node(new_sent):
            new_ocs.append(new_sent)
    return ", ".join(new_ocs)


def re_sub(sent):
    # party - party's
    # sent = re.sub(r"plaintiff ", r"plaintiff's ", sent)
    # sent = re.sub(r"plaintiffs ", r"plaintiffs' ", sent)
    # sent = re.sub(r"defendant ", r"defendant's ", sent)
    # sent = re.sub(r"defendants ", r"defendants' ", sent)
    # grant, grants - granted
    if "remand" in sent and "to remand" not in sent:
        sent = re.sub(r"remand ", r"remanded ", sent)
    sent = re.sub(r"deny |denying |denies ", r"denied ", sent)
    sent = re.sub(r"grant |granting |grants ", r"granted ", sent)
    sent = re.sub(r"sustain |sustaining |sustains ", r"sustained ", sent)
    sent = re.sub(r"overrule |overruling |overrules ", r"overruled ", sent)
    sent = re.sub(r"affirm |affirming |affirms ", r"affirmed ", sent)
    sent = re.sub(r"accept |accepting |accepts ", r"accepted ", sent)
    sent = re.sub(r"adopt |adopting |adopts ", r"adopted ", sent)
    sent = re.sub(r"reverse |reversing |reverses ", r"reversed ", sent)
    sent = re.sub(r"reject |rejecting |rejects ", r"rejected ", sent)
    sent = re.sub(r"dismissing |dismisses ", r"dismissed ", sent)
    sent = re.sub(r"recommend |recommends |recommending ", r"recommended ", sent)
    return sent


def is_sent_2node(sent):
    s = False
    a = False
    for word in sent.split():
        if word in nodes['Subject']:
            s = True
        if word in nodes['Action'] and word != 'recommended':
            a = True
        if s and a:
            return True
    return False


def sent_tokenize(sents):
    sentslist = []
    split_tag = ','
    if ';' in sents:
        split_tag = ';'
    for sent in sents.split(split_tag):
        if is_sent_2node(sent):
            sentslist.append(sent)
    return sentslist


def replace_name(p_d, sent):
    # p_d : [('henry','plaintiff'), ('davis', 'defendant')]
    words = sent.split()
    for i, word in enumerate(words):
        if "'" in word:
            name = word.split("'")[0]
            if name in p_d[0][0]:
                words[i] = p_d[0][1] + "'s"
            elif name in p_d[1][0]:
                words[i] = p_d[1][1] + "'s"
    return " ".join(words)


def sub_abbreviation(sent):
    sent = re.sub(r"r&r", r"report and recommendation ", sent)
    sent = re.sub(r"m&r", r"memorandum and recommendation ", sent)
    return sent


def drop_recommendation(s):
    s = re.sub(r"report |recommendation |memorandum ", r" ", s)
    return s


def oc_gen(sents, p_d):
    # print(">> Origin sentence: \n", sents)
    sents = sents.lower()

    if "&" in sents:
        sents = sub_abbreviation(sents)

    # drop something
    sents = re.sub(r"[^a-zA-Z0-9,;']+", r" ", sents)
    sents = re_sub(sents)

    if "recommended" in sents:
        sents = drop_recommendation(sents)

    ## replace name to plaintiff or defendant
    if p_d is not None:
        sents = replace_name(p_d, sents)

    sentslist = sent_tokenize(sents)
    # print("\n", sentslist, "\n")
    oclist = []
    for sent in sentslist:
        new_oc = rewrite_single_sent(sent) # sent - string
        if new_oc:
            oclist.append(new_oc)
            # print("\n>> Generated sentence: \n", new_oc)
    return "; ".join(oclist)


def read_case_name(own='extractor_0222', version=3, short=False):
    lni_names = {}
    ## choose short_case_name or full_case_name
    if short:
        sql_name = """SELECT distinct a.lni, b.short_case_name FROM cat_angas.outcome_label a
                    left join cat_angas.case_info b
                    on a.lni = b.lni
                    where a.own = '%s' and a.version = %d""" % (own, version)
        names_df = pd.read_sql_query(sql_name, cat_engine)
        for row in names_df.itertuples():
            _, lni, short_case_name = row
            names = short_case_name.lower()
            names = [n.strip() for n in names.split(";")]
            if len(names) == 2:
                p_d = [(names[0],'plaintiff'), (names[1], 'defendant')]
            else:
                p_d = None
            if lni not in lni_names:
                lni_names[lni] = p_d
    else:
        sql_name = """SELECT distinct a.lni, b.full_case_name FROM cat_angas.outcome_label a
                    left join cat_angas.case_info b
                    on a.lni = b.lni
                    where a.own = '%s' and a.version = %d""" % (own, version)
        names_df = pd.read_sql_query(sql_name, cat_engine)
        for row in names_df.itertuples():
            _, lni, full_case_name = row
            names = full_case_name.lower()
            split_tag = "vs." if "vs." in names else "v."
            names = [n.strip() for n in names.split(split_tag)]
            if len(names) == 2:
                p_d = [(names[0],'plaintiff'), (names[1], 'defendant')]
            else:
                p_d = None
            if lni not in lni_names:
                lni_names[lni] = p_d
    return lni_names


def main(own='extractor_0222', version=3):
    ## read case names
    lni_names = read_case_name(own, version, short=False)

    # read data
    # sql = "SELECT id, lni, sent_num FROM cat_dev.outcome_label where own='extractor_0222' and version=4"
    # cat_dev_cn = 'mysql+pymysql://charley:Abcd1234@10.123.4.222:3306/cat_dev?charset=utf8mb4'
    sql_ln = "SELECT id, lni, sent_num FROM cat_angas.outcome_label where own='%s' and version=%d" % (own, version)
    ln_df = pd.read_sql_query(sql_ln, cat_engine)

    # generate outcome
    results = []
    connection = get_connection("10.123.4.222", "charley", "Abcd1234", "cat_angas")
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        for row in ln_df.itertuples():
            _, idx, lni, sn = row
            sql_sel = """SELECT content FROM cat_angas.sentence
                    where lni = '%s' and sent_num = '%s'""" % (lni, sn)
            print(idx)
            # sql_sel = """SELECT content FROM headnote_dev.Sentence
            #         where lni = '%s' and sentnum = '%s'""" % (lni, sn)
            cursor.execute(sql_sel)
            sents = cursor.fetchall()[0]['content']
            p_d = lni_names[lni] # for replacing names
            new_sent = oc_gen(sents, p_d)
            if new_sent:
                new_sent = new_sent[0].upper() + new_sent[1:] + '.'
            else: # if '' then get origin sent
                new_sent = re.sub(r'"', r"'", sents)
            sql_u = """update cat_angas.outcome_label set predict_outcome = "%s" where id = '%d'""" % (new_sent, idx)
            # print(sql_u)
            cursor.execute(sql_u)
            # results.append( (lni, sn, sents, new_sent) )
            # print(">> ", sents)
            # print("<< ", new_sent)
            # print()
        connection.commit()
    connection.close()
    # df_3s = pd.DataFrame.from_records(results, columns=['lni', 'sent_num', 'content', 'new_oc'])
    # df_3s.to_csv('/home/micius/workspace/charley/outcome/oc_rdf/oc_neo4j_0225.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    # modified in 2019-02-27
    main(own='extractor_0222', version=4)
