class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            strx = str(x)[1:]
            out = -int(strx[::-1])
        else:
            strx = str(x)
            out = int(strx[::-1])

        if out > 2 ** 31 - 1 or out < -2 ** 31:
            return 0
        else:
            return out
