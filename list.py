nameList = ['张三', '李四', '王五', '赵六']  # JS中叫数组 Python中叫list
print(nameList)
print(len(nameList))  # len是个方法 获取到list的长度 = Js中的length
print(nameList[0])  # 获取第一个元素
print(nameList[-1])  # 获取最后一个元素 -1 即是获取到最后一个元素的索引


# List的操作
# append() 添加元素
nameList.append('赵七')
print(nameList)

# insert() 插入元素
nameList.insert(0, '张二')
print(nameList)


# pop() 删除元素
nameList.pop()  # 删除最后一个元素
print(nameList)

# pop(index) 删除指定索引的元素
nameList.pop(0)  # 删除第一个元素
print(nameList)

# 直接替换指定索引的元素
nameList[0] = '张二'
print(nameList)
