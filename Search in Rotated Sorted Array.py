'''
You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''


class Solution:
    def findLeft(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right):
            t = (right + left) // 2
            if nums[t] < nums[-1]:
                left = t + 1
            elif nums[t] <= nums[right]:
                right = t - 1
        if left == n:
            left = left - 1
        if nums[left] == target:
            return left
        else:
            return -1

    def findRight(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right):
            t = (right + left) // 2
            if nums[t] > nums[0]:
                right = t - 1
            elif nums[t] <= nums[right]:
                left = t + 1
        if right == n:
            right = right - 1
        if nums[right] == target:
            return right
        else:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        i = 0
        j = len(nums) - 1
        while(j > i):
            t = (i + j) // 2
            if nums[t] > target:
                j = t - 1
            elif nums[t] < target:
                i = t + 1
            else:
                return [self.findLeft(nums[:t], target), i + 1 + self.findRight(nums[t:], target)]
        return [i,j]


test = Solution()
print(test.searchRange([2,2], 2))
