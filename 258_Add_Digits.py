class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


class Solution:
    def addDigits(self, num: int) -> int:
        digit = str(num)
        while len(digit) != 1:
            sum1 = 0
            for i in digit:
                sum1 += int(i)
            digit = str(sum1)
        return int(digit)
