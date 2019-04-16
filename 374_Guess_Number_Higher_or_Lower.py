# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = 2 ** 24
        flag = 2
        while flag != 0:
            if guess(n) == -1:
                last = n
                n = (first + last) // 2
                flag = -1
            elif guess(n) == 1:
                first = n
                n = n = (first + last) // 2
                flag = 1
            elif guess(n) == 0:
                flag = 0
        return n


