class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先对数组进行排序（从小到大）
        # 然后从第一个到第n-2个依次作为确定的数(a)
        # 然后使用双指针的方法从右侧剩下的list中找到两个数相加等于target(0-a)
        res_list = []

        nums.sort()

        for i in range(len(nums)-2):
            res = []

            if nums[i] > 0: #如果当前最小已经>0，则不可能有3个数的和为0。
                break
            if i != 0 and nums[i] == nums[i-1]: #遇到连续相同的数就直接跳过了
                continue

            j = i + 1 #头指针
            z = len(nums)-1 #尾指针

            target = 0 - nums[i]

            while j < z:
                if nums[j] + nums[z] == target:
                    res_list.append([nums[i],nums[j],nums[z]])

                    # 重复的直接跳过
                    j += 1
                    z -= 1
                    while nums[j] == nums[j-1] and j+1 < len(nums):
                        j += 1
                    while nums[z] == nums[z+1] and z >= 0:
                        z -= 1

                elif nums[j] + nums[z] > target:
                    z -= 1
                elif nums[j] + nums[z] < target:
                    j += 1

        return res_list
