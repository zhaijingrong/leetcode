# 在数组中，寻找两数相加之和

#方法一： 遍历数组，时间复杂度为O²
def twoSum1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]
    return []

#方法二： 使用hashtable查找相差的值，将会减少一个维度的复杂度, 复杂度为O.
def twoSum2(nums, target):
    hashtable = {}
    for i, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in hashtable:
            return [hashtable[num2], i]
        hashtable[num1] = i


if __name__ == '__main__':

    nums = [2, 9, 7, 3, 11]
    target = 9

    print(twoSum1(nums, target))

    print(twoSum2(nums, target))