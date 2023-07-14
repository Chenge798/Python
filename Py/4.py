# 创建字典存储数据
data = {
    "姓名": "张三",
    "年龄": 12,
    "身高": "178cm",
    "班级": "通信2113班"
}

# 访问字典中姓名对应的值
print(data["姓名"])

# 将年龄修改为15岁，输出修改后的数据
data["年龄"] = 15
print(data)

# 以列表的形式返回字典中的所有键值对
items = list(data.items())
print(items)