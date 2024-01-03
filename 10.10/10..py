'''

给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]

示例 2：
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
'''


# 子字符不能重复， 子字符最大值

nums = list(map(int, input().split(',')))
n = len(nums)

max_num = 0
add_num = 0
# 滑动窗口方法，定义一个集合来去除重复值
start = 0
end = 0
count = set()

while end < n:
    if nums[end] in count:
        # 右指针值在里面，表示有重复数据了
        while nums[start] != nums[end]:
            add_num -= nums[start]
            count.remove(nums[start])
            start += 1
        add_num -= nums[start]
        count.remove(nums[start])
        start += 1
    # 右指针指向的值不在里面就做以下操作
    add_num += nums[end]
    count.add(nums[end])
    end += 1

    max_num = max(max_num, add_num)
print(max_num)


