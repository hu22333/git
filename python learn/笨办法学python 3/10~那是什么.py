# ex10.py
# \t为ASCII水平制表符（TAB）[\为转义]
tabby_cat = "\tI'm tabbed in."
# n换行
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a\\ cat."
# 可使用"""或者''',当字符串内部存在"时使用'''，灵活交替
# 后面为自加
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\tA
\n\tA  
\t\bB
\t\fB
\rC
"""
# 打印变量
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
