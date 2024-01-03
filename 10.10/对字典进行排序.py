
# 使用 operator 方法


import operator

# my_dict = {
#     'apple': 3,
#     'banana': 1,
#     'cherry': 2,
#     'date': 4
# }
#
# # 对字典按值排序
# sorted_dict = {key: value for key, value in sorted(my_dict.items(), key=operator.itemgetter(1))}
# print(sorted_dict)


my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 4
}

# 对字典按值排序
sorted_dict = {key: value for key, value in sorted(my_dict.items(), key=lambda item: item[1])}
print(sorted_dict)

