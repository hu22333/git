# 长度转换
# me
a = input()
if a[-1] in ['m']:
    f = (eval(a[0:-1]))*3.2808
    print("{:.2f}ft".format(f))
elif a[-1] in ['t']:
    m = (eval(a[0:-2]))/3.2808
    print("{:.2f}m".format(m))
else:
    print("格式错误")
# 标答
alen = input()
if alen[-1] == "m":
    blen = eval(alen[:-1])*3.2808
    print("{:.2f}ft".format(blen))
elif alen[-2:] == "ft":
    blen = eval(alen[:-2])/3.2808
    print("{:.2f}m".format(blen))
else:
    print("格式错误")
