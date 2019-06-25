# WordCount.py
import jieba #引入外部功能库
# 打开文件，编码格式
f = open("C:\\Users\\hu\\git\\ex\\关于中美经贸磋商的中方立场.txt", "r", encoding="utf-8")
txt = f.read() # 读入文本
f.close() # 关闭文件
ls = jieba.lcut(txt) #中文分词，调用jieba功能库中的lcut函数，用于分词
d = {} #建立空字典
for w in ls: # 利用字典
    d[w] = d.get(w, 0) + 1 # 词语统计， get() 函数返回指定键的值
for k in d: # 遍历结果（从遍历结构d中逐一提取元素，放入循环变量k中）
    if d[k] >= 50 and k != "\n": # 设置条件，次数大于50并且单次不等于换行符
        print('"{}"出现{}次'.format(k, d[k])) #打印输出
