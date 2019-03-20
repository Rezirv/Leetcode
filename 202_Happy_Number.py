class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numset = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n not in numset:
                numset.add(n)
            else:
                return False
        return True

