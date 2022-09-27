# 定义字典d1={'ab':10,'bc':2,'cd':7,'bd':6,'ac':5,'a':6,'b':3}，
# 找出关键字里面包含有字符’d’的键值对组成新的字典，并对新的字典按照value降序排序，输出结果列表。

# 字典
d1 = {'ab': 10, 'bc': 2, 'cd': 7, 'bd': 6, 'ac': 5, 'a': 6, 'b': 3}

d2 = {}
for key, value in d1.items():
    if 'd' in key:
        d2[key] = value
        pass
    pass

# 通过value值排序
lst = sorted(d2.items(), key=lambda x: x[1], reverse=True)
print(lst)
