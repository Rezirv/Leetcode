class Solution:
    def toHex(self, num: int) -> str:
        if (num == 0):
            return '0'
        hex1 = '0123456789abcdef'
        res = ''
        while (num and (len(res) < 8)):
            res = hex1[num & 0xf] + res#提取后四位
            num >>= 4 #算术移位
        return res