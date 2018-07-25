class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 在nums中遍历num,判断target-num是否在剩余的数组中
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target - num:
                    return [i,j]
        return None
