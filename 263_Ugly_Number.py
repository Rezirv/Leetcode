class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num % 2 == 0:
            if num % 2 == 1:
                return True
            else:
                num = num / 2
        while num % 3 == 0:
            if num % 3 == 1:
                return True
            else:
                num = num / 3
        while num % 5 == 0:
            if num % 5 == 1:
                return True
            else:
                num = num / 5
        if num == 1:
            return True
        else:
            return False
