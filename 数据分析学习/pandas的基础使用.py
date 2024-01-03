import pandas as pd


# Series(序列）：是pandas中的以为标记库，类似带标签的数组（哈希表？）
# DataFrame（数据框）： 二维类型的表格数据结构，由行和列组成


# 创建一个空的DataFrame
# df = pd.DataFrame()
# print(df)

# 从列表创建DataFrame
data = [['nihao', 2],
        ['world', 5],
        ['!', 10010]
        ]

df = pd.DataFrame(data)  # 行(index)、列(columns)索引默认为0、1、2、3，可以自己定义
df1 = pd.DataFrame(data, index=['1', '2', '3'], columns=['name', 'age'])
print(df)

# 如果是字典的话，已经有列索引了，如果行索引没有特别说明就不需要进行更改了


# 查看DataFrame的数据前几行， 默认5行
df.head()
# print(df.head())

# 从后面开始查找的方式
df.tail()

# 查看列名和索引
df.columns
df.index

# 查看统计信息   主要有count、mean、std、min、max
# print(df.describe())


# 选择列 和 选择多列
print('验证是否和我已有知识的相似性：')
print('index:', df[[0, 1]])
df[[0, 1]]  # 多列

# 条件选择器
tt = df[df[1] > 20]
print('tt:', tt)


# 删除指定中的列
df.drop()  # axis 在这里与前面的相反，

# 转时间序列类型
pd.to_datetime()
# 设置索引,可以将某一列作为索引
df.set_index()

# 布尔值可以作为行索引，去除True对应的行数据