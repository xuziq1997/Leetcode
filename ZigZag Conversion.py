class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1:
            return s
        suffix = [['' for x in range(n)] for y in range(numRows)]
        start = 0
        answer = ''

        for i in range(n):
            for j in range(numRows):
                if start < n:
                    if i % (numRows - 1) == 0:
                        suffix[j][i] = s[start]
                        start += 1
                    elif (i % (numRows - 1)) == numRows - j - 1:
                        suffix[j][i] = s[start]
                        start += 1
                    else:
                        suffix += 'skip'
                else:
                    break

        for j in range(numRows):
            for i in range(n):
                if suffix[j][i] == 'skip' or suffix[j][i] == '':
                    pass
                else:
                    answer += suffix[j][i]
        return answer

test = Solution()
print(test.convert("A", 1))

