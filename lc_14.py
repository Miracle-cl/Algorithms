# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.



def longestCommonPrefix(strs):
	if strs:
		for i, tup in enumerate(zip(*strs)):
			if len(set(tup)) > 1:
				return strs[0][:i]
		else:
			return min(strs)
	else:
		return ''

strs = ['', '']
print(longestCommonPrefix(strs))
# longestCommonPrefix1(strs)
