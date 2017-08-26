# title: Longest Substring Without Repeating Characters
#
# description: Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
	length = len(s)
	result = []
	rs = ''
	# List of Substring Without Repeating Characters
	for i in range(length):
		string = s[i:]
		for st in string:
			if st not in rs:
				rs += st
			else:
				break
		result.append(rs)
		rs = ''

	# Longest Substring in List of Substring
	longest = result[0]
	for ele in result:
		if len(ele) > len (longest):
			longest = ele
	return len(longest)
