class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = ''
        if num // 1000:
            answer = answer + (num // 1000) * 'M'
            num = num % 1000

        if num // 100:
            b = num // 100
            if b == 9:
                answer = answer + 'CM'
            elif b == 4:
                answer = answer + 'CD'
            elif b >= 5:
                answer = answer + 'D' + 'C' * (b - 5)
            else:
                answer = answer + 'C' * b
            num = num % 100

        if num // 10:
            c = num // 10
            if c == 9:
                answer = answer + 'XC'
            elif c == 4:
                answer = answer + 'XL'
            elif c >= 5:
                answer = answer + 'L' + 'X' * (c - 5)
            else:
                answer = answer + 'X' * c
            num = num % 10

        if num:
            d = num
            if d == 9:
                answer = answer + 'IX'
            elif d == 4:
                answer = answer + 'IV'
            elif d >= 5:
                answer = answer + 'V' + 'I' * (d - 5)
            else:
                answer = answer + 'I' * d

        return answer

test = Solution()
print(test.intToRoman(4))