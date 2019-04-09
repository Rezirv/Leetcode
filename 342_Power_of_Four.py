class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        flag1 = num&(num-1)
        flag2 = num&0xAAAAAAAA
        if num <= 0:
            return False
        elif flag1 == 0 and flag2 == 0:
            return True
        else:
            return False