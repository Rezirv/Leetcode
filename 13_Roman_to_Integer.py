class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        for i in s[::-1]:
            flag = 1
            if (i in ['I', 'X', 'C']) and result >= dict[i] * 5:
                flag = -1
            result += flag * dict[i]
        return result

