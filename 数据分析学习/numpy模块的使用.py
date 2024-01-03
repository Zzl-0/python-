import numpy as np # 数据分析三剑客 numpy, pandas, matplotlib
import matplotlib
from matplotlib import pyplot as plt, pylab

# 使用numpy创建数组
arr = np.array([1, 2, 3])   # 自定义，自输入创建

# 数组和列表的区别（可能考点）
#   数组中存储的数据类型必须是统一类型 优先级为 字符串》浮点》整形
#   列表中，可以存储不同数据类型
# 1. 例子
arr1 = np.array([1, 2.2, "nihao"])
# print(arr1)  # ['1' '2.2' 'nihao']

arr2 = np.array([1, 2.2, 3])
# print(arr2)  # [1.  2.2 3. ]


# 将外部数组读取到numpy数组中，改变数组元素对原始图片的影响
img_arr = plt.imread('./assets/test.png', '.png')  # 记录bug日志 1
# print(img_arr)  # 图片二进制编码

# 可视化展示
plt.imshow(img_arr)
# pylab.show()


# 将数组元素都减去100的色调
img_arr1 = img_arr.copy()
img_arr1 -= 100
plt.imshow(img_arr1)
# pylab.show()


# 其他使用
# np.linespace()  # 不知道版本有没有迭代更新


# 二、numpy常用属性
# 1. shape 维度  2. dtype 类型  3.
# print(arr.shape)


# 索引操作
arr_index = np.random.randint(1, 100, size=(3, 4))
# print(arr_index)  #[[39 70 78 33], [39 17 63 17], [46 17 90 18]]
# print(arr_index[1])  # [39 17 63 17]
# 取出多行  arr_index[[1,2]]
arr_index[0:2]  # 前两列
arr_index[0:2, 0:2]  # , 分割行和列


# 以上的学习可以将数组元素进行切片，倒置等，那么图片可以转化为二进制进数组，图片也可以进行更改
plt.imshow(img_arr[:, ::-1])
# pylab.show()

plt.imshow(img_arr[::-1, :])
# pylab.show()

# 图片裁剪功能
plt.imshow(img_arr[50:620, 0:790])
# pylab.show()


# 级联操作 关键字 concatenate  只能同一维度进行级联，
arr4 = np.random.randint(1, 6, 3)
test = np.concatenate((arr4, arr), axis=0)  # axis =0 是级联行， =1 是级联列
print(test)


# 数据分析中常常使用某些形势的运算来处理原始数据，如果原数据中的空值为NaN形式就不会干扰到运算的进行
# 两种空值  None    NAN（尽量使用）
# isNull -> any 用来检测行或列中是否存在True   notNull -> all 用来检测false
# dropna  可以直接将缺失的行或者列进行删除 或者 要删除的数据过多 可以进行覆盖  fillna
