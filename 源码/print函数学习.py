# 可以输出数字
print("520")

# 可以输出字符
print("Hellow world")

# 含有运算符的表达式
print(2 + 5)

# 可以将数据输出到文件中,注意，1.所指定的盘符要存在。2.使用file=fp。
fp = open("F:/print函数学习.txt", "a+")  # 如果文件不存在就创建，存在就在文件内容后面继续追加
print("Hellow world", file=fp)
fp.close()

# 进行不换行输出（输出内容在同一行中）
print("hellow", "world", "python")
