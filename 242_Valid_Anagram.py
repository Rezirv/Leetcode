class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = [0] * 26
        list2 = [0] * 26
        for i in s:
            list1[ord(i) - ord('a')] += 1
        for i in t:
            list2[ord(i) - ord('a')] += 1
        return list1 == list2


