from collections import Counter
from operator import itemgetter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def helper(formula):
            res = Counter()
            size = len(formula)
            i = 0
            while i < size:
                if formula[i] == '(':
                    i += 1
                    beg_id = i
                    cnt = 1
                    while cnt != 0:
                        if formula[i] == '(':
                            cnt += 1
                        elif formula[i] == ')':
                            cnt -= 1
                        i += 1
                    tmp = helper(formula[beg_id:i-1])
                    numbers = ''
                    while i < size and formula[i].isdigit():
                        numbers += formula[i]
                        i += 1
                    numbers = int(numbers) if numbers else 1
                    for k, v in tmp.items():
                        res[k] += v * numbers

                elif formula[i].isupper(): # 'A' <= formula[i] <= 'Z':
                    k = formula[i]
                    i += 1
                    while i < size and formula[i].islower():
                        k += formula[i]
                        i += 1
                    numbers = ''
                    while i < size and formula[i].isdigit():
                        numbers += formula[i]
                        i += 1
                    numbers = int(numbers) if numbers else 1
                    res[k] += numbers

            return res
        res = helper(formula)
        res = sorted(res.items(), key=itemgetter(0))
        return ''.join([k + (str(v) if v > 1 else '') for k, v in res])


class Solution1:
    def countOfAtoms(self, formula: str) -> str:
        def get_number(formula, i):
            numbers = ''
            while i < len(formula) and formula[i].isdigit():
                numbers += formula[i]
                i += 1
            numbers = int(numbers) if numbers else 1
            return numbers, i
        
        def get_atom(formula, i):
            atom = formula[i]
            i += 1
            while i < len(formula) and formula[i].islower():
                atom += formula[i]
                i += 1
            return atom, i

        def helper(formula, i):
            res = Counter()
            while i < len(formula):
                if formula[i] == '(':
                    tmp, i = helper(formula, i+1)
                    numbers, i = get_number(formula, i)
                    for k, v in tmp.items():
                        res[k] += v * numbers
                elif formula[i] == ')':
                    i += 1
                    return res, i
                else:
                    atom, i = get_atom(formula, i)
                    numbers, i = get_number(formula, i)
                    res[atom] += numbers
            return res, i
        
        res, _ = helper(formula, 0)
        res = sorted(res.items(), key=itemgetter(0))
        return ''.join([k + (str(v) if v > 1 else '') for k, v in res])


if __name__ == '__main__':
    solu = Solution1()
    formula = "K4(ON(SO3)2)2"
    res = solu.countOfAtoms(formula)
    print(res)
