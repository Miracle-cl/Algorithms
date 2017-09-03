# title: Longest Palindromic Substring
#
# description: Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Examples:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""
	length = len(s)
	flag = 0
	for i in range(length):
		li = length - i
		for j in range(i+1):
			s1 = s[j:j+li]
			if s1 == s1[::-1]:
				return s1
	else:
		return 'none'
strs = "miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenz"
print(longestPalindrome(strs))

# li - i+1 -i
# 5-1-0
# 4-2-1
# 3-3-2
# 2-4-3
