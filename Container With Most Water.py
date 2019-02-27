class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        start = 0
        end = len(height) - 1
        while(end - start > 0):
            area = (end - start) * min(height[start], height[end])
            if area > max:
                max = area
            if min(height[start], height[end - 1]) > min(height[start + 1], height[end]):
                end = end - 1
            else:
                start = start + 1
        return max


test = Solution()
print(test.maxArea([1,3,2,5,25,24,5]))