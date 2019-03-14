class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        strdict = {i: chr(i + 64) for i in range(1, 27)}
        res = ''
        while n:
            n, b = divmod(n, 26)
            if b == 0:
                b = 26
                n -= 1
            res = strdict[b] + res
        return res
