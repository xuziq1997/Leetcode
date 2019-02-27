'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S='', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
            if left < n:
                backtrack(S + '(', left+1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()

        return ans
