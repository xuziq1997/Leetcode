'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
'''
class Solution:
    def calculate_area(self, s):
        r = 0
        if len(s) <= 2:
            return 0
        else:
            for i in s[1:-1]:
                r = r + max(min(s[0], s[-1]) - i, 0)
        return r

    def find_max(self, s):
        n = len(s)
        if n <= 2:
            return 0
        index = 0
        max = 0
        i = 1
        while(i < n):
            if s[i] > s[0]:
                return i
            elif s[i] >= max:
                max = s[i]
                index = i
            i = i + 1
        return index

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        ans = 0
        while(i != n-1):
            j = self.find_max(height[i:]) + i
            ans = ans + self.calculate_area(height[i:j + 1])
            i = j
        return ans



test = Solution()
print(test.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


