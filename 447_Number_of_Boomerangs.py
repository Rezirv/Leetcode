import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:  #三个为一组，以中间的元祖为中心，将所有和它距离相同的放在一个字段中计数，然后每一组计算一次
            count = {}
            for j in points:
                if i != j:
                    distace = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                    if distace in count:
                        count[distace] += 1
                    else:
                        count[distace] = 1
            for k in count.values():
                if k >= 2:
                    res += k * (k - 1)
        return res
