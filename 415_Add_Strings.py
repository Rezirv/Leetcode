class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for i in range(1, len(num1) + 1):
            str_2 = 0 if len(num2) < i else int(num2[-i])
            r = str_2 + int(num1[-i]) + carry
            res.append(str(r % 10))
            carry = r // 10
        if carry != 0:
            res.append(str(carry))
        res.reverse()
        return ''.join(res)
