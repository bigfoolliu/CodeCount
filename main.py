#!-*-coding:utf-8-*-
# !@Date: 2018/8/17 9:23
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
思路:

"""

import os

search_path = "D:/PythonProjects/LittleGame"
code_file_list = list()  # 搜索目录下的所有.py文件路径列表

blank_line_list = list()  # 空白行列表
notation_line_list = list()  # 注释行列表
code_line_list = list()  # 代码行列表

walk_list = list(os.walk(search_path))  # 返回搜索路径的三元组的列表

# 测试
print("=" * 50)
print("walk_list:")
for item in walk_list:
	print(item)
print("=" * 50)

# 遍历查找所有的.py文件
for walk_tuple in walk_list:
	for file in walk_tuple[2]:
		file_path = os.path.join(walk_tuple[0], file)
		if file_path.endswith(".py"):
			code_file_list.append(file_path)

# 测试,将所有.py文件显示出来
print("=" * 50)
print("code_file_list:")
for item in code_file_list:
	print(item)
print("=" * 50)


for code_file in code_file_list:
	with open(code_file, "r", encoding="utf-8") as f:
		content = f.readlines()  # 读取文件行列表
		print(len(content))  # 文件行数
		for line in content:
			_line = line.strip()  # 将首尾的空格去除
			if not _line:  # 该行为空格,什么都没有
				blank_line_list.append(_line)
			elif _line.startswith("#"):  # 该行以#开头
				notation_line_list.append(_line)
			else:
				code_line_list.append(_line)


print("=" * 50)
print("结果:")
print("代码行: ", len(code_line_list))
print("空白行: ", len(blank_line_list))
print("注释行: ", len(notation_line_list))
print("总行数: ", len(code_line_list) + len(blank_line_list) + len(notation_line_list))
print("=" * 50)

