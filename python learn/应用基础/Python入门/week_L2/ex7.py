# 英文单次个数统计
# replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)
s = '''
"Collusion is very real with Russia," Trump quoted conservative commentator Dan Bongino as saying on Trump's favorite Fox News morning show, "but only with Hillary and the Democrats, and we should demand a full investigation."
'''
s = s.replace('"', ' ')
s = s.replace(',', ' ')
s = s.replace('.', ' ')
ls = s.split()
print(len(ls))

# 统计单词个数，一个重要环节是去掉标点符号。这里采用将标点符号替换为空格的方式。
# 使用字符串s.replace(old, new)方法，能够将字符串中old子串替换为new子串。
# 也可以逐一遍历字符串进行处理
