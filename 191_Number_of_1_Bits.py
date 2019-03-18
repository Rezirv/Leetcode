class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1 = bin(n)[2:]
        flag = 0
        for i in list(str1):
            if i == '1':
                flag += 1
        return flag