# title: Valid Parentheses
#
# description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# 使用栈解决问题

def isValid(s):
	stack = []
	for i in range( len(s) ):
		if s[i] in ['(', '[', '{']:
			stack.append(s[i])
		if s[i] == ')':
			if stack == [] or stack.pop() != '(':
				return False
		if s[i] == ']':
			if stack == [] or stack.pop() != '[':
				return False
		if s[i] == '}':
			if stack == [] or stack.pop() != '{':
				return False
	if not stack:
		return True
	else:
		return False

print(isValid('([{()()}])'))
