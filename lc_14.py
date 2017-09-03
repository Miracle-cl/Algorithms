# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.


def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	if strs:
		l = len(strs[0])
		if len(strs) > 1:
			flag = 0
			for i in range(l):
				st = strs[0][:i+1]
				for string in strs:
					if st not in string:
						flag = 1
						break
				if flag:
					break
			return strs[0][:i]
		else:
			return min(strs)
	else:
		return ''


def longestCommonPrefix1(strs):
	if strs:
		for i, tup in enumerate(zip(*strs)):
			if len(set(tup)) > 1:
				return strs[0][:i]
		else:
			return min(strs)
	else:
		return ''

strs = ['aaaa', 'aa', 'aab']
print(longestCommonPrefix1(strs))
# longestCommonPrefix1(strs)
