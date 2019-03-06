class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        i = 1
        num = 0
        last = []
        while length - 1 >= 0:
            num += digits[length - 1] * i
            length -= 1
            i *= 10
        for j in str(num + 1):
            last.append(int(j))
        return last
