class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            lt = haystack.split(needle, 1)
            if len(lt[0]) == len(haystack):
                return -1
            else:
                return len(lt[0])

