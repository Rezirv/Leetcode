from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dict1 = Counter(s)
        odd = 0
        eve = 0
        flag = 0
        for i in dict(dict1).values():
            if i % 2 == 0:
                odd += i
            else:
                flag = 1
                eve += i - 1
        if flag == 0:
            return odd
        else:
            return odd + eve + 1
