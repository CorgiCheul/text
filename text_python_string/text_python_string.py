# 熟练掌握并使用字符串用法
# 1.定义一个字符串”Hello World!"，并打印
str = "Hello World!"
print(str)
# 2.将"1"中的字符串切片，长度为从第2个字符开始，第7个字符结束，并打印
str_cut1 = str[1:8]
print(str_cut1)
# 3.将"1"中的字符串切片，长度为从第1个字符开始，第8个字符结束，步长为2，并打印
str_cut2 = str[0:9:2]
print(str_cut2)
# 4.将"1"中的字符串中所有字符”o“，替换为”T“，并打印
str_replace = str.replace("o", "T")
print(str_replace)
# 5.将"1"中的字符串与4中的字符串拼接，并打印
str_double = str + str_replace
print(str_double)
# 6.查找"2"中字符串中所有的字符”o“所处的位置，并打印
str_find_o1 = str_cut1.find("o")
str_find_o2 = str_cut1.find("o", 4, 10)
print(str_find_o1)
print(str_find_o2)
# 7.查找”3“中字符串中所有的字符”H"出现的次数,并打印
str_count = str_cut2.count("H")
print(str_count)
# 8.将“1”中的字符串在保持句意不变的情况下，分割成两个部分，并打印
str_split = str.split(" ")
print(str_split)
# 9.请将下列字符串按字符“，”分割，并打印
#   “我叫李磊，今年18岁，我喜欢韩梅梅”
str_2 = "我叫李磊，今年18岁，我喜欢韩梅梅"
str_2_split = str_2.split("，")
print(str_2_split)
# 10.请去除下列字符串的空格，使其可以以向左对齐的方式打印
#    "   Hello World!   "
str_3 = "   Hello World!   "
str_3_strip = str_3.strip()
print(str_3_strip)
# 11.请去除下列字符串中的无用字符，使其成为一段完整的句子，并打印
#   ”sssaysyasyHello World!yysassaa"
str_4 = "sssaysyasyHello World!yysassaa"
str_4_strip = str_4.strip("say")
print(str_4_strip)
# 12.请用合适的占位符，补充下列句子的空白处,并使用占位符的语法将数据补充完整，并打印
#   我叫  ，今年  岁，我喜欢  。
str_5 = "我叫%s,今年%d岁,我喜欢%s。" % ("李磊", 18, "韩梅梅")
print(str_5)
# 13.将“12”中的字符串用F表达式展示，并打印
name = "李磊"
age = "18"
hobby = "韩梅梅"
str_6 = F"我叫{name},今年{age}岁,我喜欢{hobby}"
print(str_6)
# 14.请计算“1”中的字符串的长度，并打印
print(len(str))
# 15.请使用格式化输出的方法展现下列数据
#    pai = 3.141592653589796
# （1）以百分比形式打印(保留两位小数)
pai = 3.141592653589796
print("圆周率{:.2%}".format(pai))
# （2）保留5位小数并打印
print("圆周率{:.5f}".format(pai))
# 16.将下列字符串转换为大写，并打印
# "hello world!"
str_7 = "hello world!"
print(str_7.upper())
# 17.将下列字符串转换为小写，并打印
# "HELLO WORLD!"
str_8 = "HELLO WORLD!"
print(str_8.lower())
#在控制台输入空白信息，使得下列字符串完整，并打印
#    "我叫{},今年{},我喜欢{}"
str_9="我叫{},今年{},我喜欢{}"
name=input("请输入姓名")
age=input("请输入年龄")
hobby=input("请输入爱好")
str_10=str_9.format(name,age,hobby)
print(str_10)