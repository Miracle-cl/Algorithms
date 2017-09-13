# title:  Letter Combinations of a Phone Number
#
# description: Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Examples:
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


def letterCombinations(digits):
	a = ['2', '3', '4', '5', '6', '7', '8', '9']
	b = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
	d = dict(zip(a, b))

	r = ''
	for numstr in digits:
		if numstr not in ['0', '1']:
			r += numstr
	if r:
		l = []
		for numstr in r:
			l.append(d[numstr])

		num = len(l)
		l0 = []
		for i in range(num):
			if l0:
				le = []
				for x in l0:
					for y in list(l[i]):
						le.append( x + y )
				l0 = le
			else:
				l0 = list(l[i])
	else:
		l0 = []

	return l0

digits = '123'
res = letterCombinations(digits)

print(res)
print(len(res))
