# 传感器日志光照统计
# me（忘了关闭文件）
f = open("sensor-data-1k.txt", "r")
count, num = 0, 0
for line in f:
    ls = line.split()
    num += eval(ls[4])
    count += 1
print("{:.2f}".format(num/count))

# 标答
f = open("sensor-data-1k.txt", "r")
sum, cnt = 0, 0
for line in f:
    ls = line.split()
    cnt += 1
    sum += eval(ls[4])
print("{:.2f}".format(sum/cnt))
f.close()
