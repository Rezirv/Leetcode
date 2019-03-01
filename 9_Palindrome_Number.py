class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        palindrome_x = strx[::-1]
        if strx == palindrome_x:
            return True
        else:
            return False
