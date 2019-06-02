class Solution:
    def compress(self, chars: List[str]) -> int:
        num = 1
        for i in range(len(chars) - 1, 0, -1):  # 该题是相同字母都堆积在一起，利于从后面遍历
            if chars[i] == chars[i - 1]:
                num += 1
                del (chars[i])
            else:
                if num > 1:
                    chars[i + 1:i + 1] = list(str(num))  # 在i位置后面插入重复数
                num = 1
        if num > 1:
            chars[1:1] = list(str(num))  # list[1:1]可以在1这个位置插入值
        return len(chars)







