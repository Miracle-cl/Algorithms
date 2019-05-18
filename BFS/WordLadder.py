# =========================== problem 1 ===========================
class Solution_length:
    def ladderLength(self, beginWord='hit', endWord='cog', wordList=["hot","dot","dog","lot","log","cog"]):
        if (not wordList) or (not wordList[0]) or (endWord not in wordList):
            return 0
        charset = set("".join(wordList + [beginWord, endWord]))
        wordset = set(wordList)

        length = 1
        queue = [(beginWord, length)]
        while len(queue) > 0 and len(wordset) > 0:
            word, length = queue.pop(0)
            for i in range(len(word)):
                for char in charset:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word == endWord:
                        return length + 1
                    if new_word in wordset:
                        wordset.remove(new_word)
                        queue.append((new_word, length+1))
        return 0

s = Solution_length()
length = s.ladderLength()


# =========================== problem 2 ===========================
beginWord='hit'
endWord='cog'
wordList=["hot","dot","dog","lot","log","cog"]

beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
# out = [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]

class RightSolution:
    # time and space is OK.
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        wordset = set(wordList)
        p = [beginWord]
        queue_paths = []
        queue_paths.append(p)
        level = 1
        minLevel = len(wordList) + 1
        words = set()
        charset = "abcdefghijklmnopqrstuvwxyz"
        while queue_paths:
            t = queue_paths.pop(0)
            if len(t) > level:
                for w in words:
                    wordset.remove(w)
                words.clear()
                level = len(t)
                if level > minLevel:
                    break
            last = t[-1]
            for i in range(len(last)):
                for char in charset:
                    new_last = last[:i] + char + last[i+1:]
                    if new_last not in wordset:
                        continue
                    words.add(new_last)
                    nextPath = t
                    nextPath.append(new_last)
                    if new_last == endWord:
                        res.push_back(nextPath)
                        minLevel = level
                    else
                        queue_paths.append(nextPath)
        return res


# # =========================== time limit exceeded ===========================
class TreeNode:
    def __init__(self, word):
        self.val = word
        self.next = None
        self.parent = None

class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, parent, child):
        # parent child is both node
        if parent.next is None:
            parent.next = [child]
        else:
            parent.next.append(child)

    def find_parents(self, child):
        path = [child.val]
        while (child.parent is not None):
            child = child.parent
            path.append(child.val)
        return path

class S1:
    def create_tree(self, beginWord, endWord, wordList):
        root = TreeNode(beginWord)

        tree = Tree(root)
        charset = set("".join(wordList + [beginWord, endWord]))
        wordset = set(wordList)
        wordset.remove(endWord)

        queue = [root]
        while len(queue) > 0:
            root = queue.pop(0)
            word = root.val
            if word == endWord:
                continue
            parents = set(tree.find_parents(root))
            for i in range(len(word)):
                for char in charset:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word == endWord:
                        node = TreeNode(new_word)
                        node.parent = root
                        queue.append(node)
                        tree.insert(root, node)

                    elif (new_word in wordset) and (new_word not in parents):
                        # wordset.remove(new_word)
                        node = TreeNode(new_word)
                        node.parent = root
                        queue.append(node)
                        tree.insert(root, node)
        return tree

    def findLadders(self, beginWord, endWord, wordList):
        if (not wordList) or (not wordList[0]) or (endWord not in wordList):
            return []
        tree = self.create_tree(beginWord, endWord, wordList)
        paths = []
        q = []
        q.append(tree.root)
        while q:
            n = q.pop(0)
            #print(n.val, n.parent.val if n.parent is not None else n.parent)
            if n.val == endWord:
                path = tree.find_parents(n)
                path.reverse()
                if paths and len(paths[0]) == len(path):
                    paths.append(path)
                elif not paths:
                    paths.append(path)

            if n.next is not None:
                for child in n.next:
                    q.append(child)
        return paths


# # =========================== time limit exceeded ===========================
class TreeNode:
    def __init__(self, word, level):
        self.val = word
        self.level = level
        self.next = None
        self.parent = None

class S2:
    def findLadders(self, beginWord, endWord, wordList):
        if (not wordList) or (not wordList[0]) or (endWord not in wordList):
            return []
        root = TreeNode(beginWord, 1)

        tree = Tree(root)
        charset = set("".join(wordList + [endWord]))
        wordset = set(wordList)
        wordset.remove(endWord)
        paths = []

        queue = [root]
        prev_words = set([beginWord])
        pre_level = 1
        cur_words = []
        end_level = len(wordList) + 1
        while len(queue) > 0:
            root = queue.pop(0)
            word = root.val

            if root.level >= end_level:
                break

            if root.level - pre_level > 1:
                pre_level += 1
                prev_words = prev_words | set(cur_words)
                wordset = wordset - prev_words
                cur_words.clear()
            cur_words.append(word)

            if word == endWord:
                continue # useless

            for i in range(len(word)):
                for char in charset:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word == endWord and root.level < end_level:
                        end_level = root.level + 1
                        node = TreeNode(new_word, root.level+1)
                        node.parent = root
                        queue.append(node)
                        tree.insert(root, node)

                        parents = tree.find_parents(node)
                        parents.reverse()
                        paths.append(parents)

                    elif (new_word in wordset):
                        node = TreeNode(new_word, root.level+1)
                        node.parent = root
                        queue.append(node)
                        tree.insert(root, node)

        return paths


# # =========================== time limit exceeded ===========================
class TreeNode:
    def __init__(self, word, level):
        self.val = word
        self.level = level
        self.next = None

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if (not wordList) or (not wordList[0]) or (endWord not in wordList):
            return []
        root = TreeNode(beginWord, 1)

        charset = set("".join(wordList + [endWord]))
        wordset = set(wordList)
        wordset.remove(endWord)
        paths = []

        queue = [[root]]
        prev_words = set([beginWord])
        pre_level = 1
        cur_words = []
        end_level = len(wordList) + 1
        while len(queue) > 0:
            node_list = queue.pop(0)
            root = node_list[-1]
            word = root.val

            if root.level >= end_level:
                break

            if root.level - pre_level > 1:
                pre_level += 1
                prev_words = prev_words | set(cur_words)
                wordset = wordset - prev_words
                cur_words.clear()
            cur_words.append(word)

            for i in range(len(word)):
                for char in charset:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word == endWord and root.level < end_level:
                        end_level = root.level + 1
                        paths.append([node.val for node in node_list] + [endWord])
                    elif (new_word in wordset):
                        node = TreeNode(new_word, root.level+1)
                        queue.append(node_list + [node])

        return paths
