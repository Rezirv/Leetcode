class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        i = 1
        while i:
            if 2 ** i == n:
                return True
            elif 2 ** (i - 1) < n and 2 ** (i) > n:
                return False
            else:
                i += 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            b = bin(n)[2:]
            num = 0
            for i in b:
                if i == '1':
                    num += 1
            if num > 1:
                return False
            else:
                return True

