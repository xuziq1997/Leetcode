'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        max_i = len(nums)-1
        i = 0
        while i <= max_i:
            if nums[i] == val:
                nums.pop(i)
                print(nums)
                max_i -= 1
            else:
                i += 1
        return len(nums)
