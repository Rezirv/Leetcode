class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 因为从2开始才有第一个质数
        if n < 3:
            return 0
        else:
            list1 = [1] * n
            list1[0] = list1[1] = 0
            for i in range(2, int(n ** 0.5) + 1):
                if list1[i] == 1:
                    list1[i * i:n:i] = [0] * len(list1[i * i:n:i])
            return sum(list1)
