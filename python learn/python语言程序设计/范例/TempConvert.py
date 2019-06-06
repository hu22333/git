# TempConvert.py
TempStr = input("请输入带有符号的温度值：")#输入温度
if TempStr[-1] in ['F', 'f']:#倒数第一位是否为F，或f
    C = (eval(TempStr[0:-1])-32)/1.8 #切片截取最后一位并去引号然后执行
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}f".format(F))
else:
    print("输入格式错误")


