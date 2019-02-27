'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n):
            j = i + 1
            k = n - 1
            t = target - nums[i]
            while (j < k):
                if abs(nums[j] + nums[k] - t) >= abs(res-target):
                    if nums[j] + nums[k] - t > 0:
                        k = k - 1
                    else:
                        j = j + 1
                else:
                    res = nums[i] + nums[j] + nums[k]
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    if res < target:
                        j = j + 1
                    elif res > target:
                        k = k - 1
                    else:
                        return res

        return res

test = Solution()
print(test.threeSumClosest([0,2,1,-3], 1))