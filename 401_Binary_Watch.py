class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        out = []
        for i in range(12):
            for j in range(60):
                if (self.count(i) + self.count(j) == num):
                    minute = str(j) if j >= 10 else '0' + str(j)
                    out.append(str(i) + ':' + minute)
        return out

    def count(self, n):
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res
                                                                                              