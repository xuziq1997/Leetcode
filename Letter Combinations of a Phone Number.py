'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        match = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                 '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = [digits]
        n = len(digits)

        for i in range(n):
            new_res = []
            for s in res:
                t = s
                for j in match[s[i]]:
                    t = t[:i] + j + t[i + 1:]
                    new_res.append(t)
            res = new_res
        return res

test = Solution()
print(test.letterCombinations(''))


