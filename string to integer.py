class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        """
        :type str: str
        :rtype: int
        """
        valid='1234567890-+'
        number_str='0123456789'
        is_first_non_blank=False
        is_number_involved=False
        number=''
        for letter in str:
            if is_first_non_blank:
                if letter not in number_str:
                    break
                else:
                    number += letter
            else:
                if letter == ' ':
                    continue
                else:
                    is_first_non_blank=True
                    if letter in number_str:
                        is_number_involved=True
                    number += letter
        if number == '':
            return 0
        try:
            ans = int(number)
        except:
            return 0
        if ans >= 2 ** 31:
            return 2 ** 31-1
        elif ans <= -2 ** 31:
            return -2 ** 31
        else:
            return ans



trial=Solution()
x = trial.myAtoi()
print(x)