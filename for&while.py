names = ['张三', '李四', '王五', '赵六']
for name in names:
    print(name)

sum = 0
for i in range(101):
    sum += i
print(sum)

# range(101) 可以生成一个整数序列
# 序列是从0开始
# Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表

print(list(range(101)))


# while循环，只要条件满足，就不断循环，条件不满足时退出循环
index = 0
total = 100
while total > 0:
    index = total+index
    total = total - 1

print(index)
