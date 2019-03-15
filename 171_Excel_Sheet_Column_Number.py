class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        strdict = {chr(i+64): i for i in range(1, 27)}
        res = 0
        news = list(s)
        i = 0
        while news:
            res += (strdict[news[-1]])*(26**i)
            i += 1
            news.pop()
        return res