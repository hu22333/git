# SensorReader.py
try:  # 异常处理
    f = open('C:\\Users\\hu\\git\\ex\\sensor-data-1k.txt', 'r')  # 打开文件，设置绝对路径
    avg, cnt = 0, 0  # 变量初值
    for line in f:
        ls = line.split() #split() 通过指定分隔符对字符串进行切片，保存在列表中
        cnt += 1 # 统计行数
        avg += eval(ls[2]) #计算总和
    print("平均的温度值是：{:.2f}".format(avg/cnt)) #
    f.close()  # 文件关闭
except:
    print("文件打开错误")

#注 python在描述路径时可以有多种方式
#方式一:转义的方式
#'d:\\a.txt'

#方式二:显式声明字符串不用转义
#'d:r\a.txt'

#方式三:使用Linux的路径/
#'d:/a.txt'

