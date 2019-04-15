class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        flag = 1
        while num > 0:
            num -= flag
            flag += 2
        return num == 0
