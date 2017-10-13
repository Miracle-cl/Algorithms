import itertools


def sum24(s):
	return eval(s)

def judegPoint24(numlist):
	"""24 game"""
	# 表达式=数字组合
	all_numlist = []
	count = 0
	for numtup in itertools.permutations(numlist,4):
		strlist = [str(num) for num in numtup]
		all_numlist.append(strlist)


	# 表达式=数字组合+运算符号组合
	# 运算符号组合
	operations = ['+', '-', '*', '/']
	all_opslist = [[x, y, z] for x in operations for y in operations for z in operations]

	# 数字+运算符
	expression = [] # 表达式
	for num in all_numlist:
		for ops in all_opslist:
			ops.append('')
			expression.append( list(zip(num, ops)) )

	# 将表达式中的 元祖列表 转为 str组成的表达式：[('1', '+'), ('7', '+'), ('8', '-'), ('3', '')] ~ 1+7+8-3
	expression_str = [] # 表达式
	for explist in expression:
		astr = ''
		for i in explist:
			astr += ''.join(i)
		expression_str.append(astr)
	# print(len(expression_str))

	# 插入2对括号：
	expression_str1 = [] # 表达式
	for estr in expression_str:
		for i in range(len(estr)):
			expression_str1.append( estr[:i] + '(' + estr[i:] )
	# print(len(expression_str1))

	expression_str2 = [] # 表达式
	for estr in expression_str1:
		for i in range(1,len(estr)+1):
			expression_str2.append( estr[:i] + ')' + estr[i:] )
	# print(len(expression_str2))

	expression_str3 = [] # 表达式
	for estr in expression_str2:
		for i in range(len(estr)):
			expression_str3.append( estr[:i] + '(' + estr[i:] )
	# print(len(expression_str3))

	expression_str4 = [] # 表达式
	for estr in expression_str3:
		for i in range(1,len(estr)+1):
			expression_str4.append( estr[:i] + ')' + estr[i:] )
	# print(len(expression_str4))

	flag = 0
	for estr in expression_str4:
		try:
			if abs(sum24(estr) - 24) < 0.0000001:
				flag = 1
				return estr
				break
		except:
			pass

	return bool(flag)

numlist = [3,8,8,3]
print(judegPoint24(numlist))
