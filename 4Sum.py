'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        res = []
        nums = sorted(nums)

        for i in range(n-3):
            for j in range(i+1, n-2):
                t = target - nums[i] - nums[j]
                k = j + 1
                l = n - 1
                while(k < l):
                    if nums[k] + nums[l] > t:
                        l = l - 1
                    elif nums[k] + nums[l] < t:
                        k = k + 1
                    else:
                        if [nums[i], nums[j], nums[k], nums[l]] in res:
                            pass
                        else:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        while (k < l and nums[k] == nums[k + 1]):
                            k = k + 1
                        k = k + 1
                        while (k < l and nums[l] == nums[l - 1]):
                            l = l - 1
                        l = l - 1
        return res

test = Solution()
print(test.fourSum([1, 0, -1, 0, -2, 2], 0))
