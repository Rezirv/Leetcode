class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = [0]*26
        mag = [0]*26
        for i in ransomNote:
            ran[ord(i)-ord('a')] += 1
        for i in magazine:
            mag[ord(i)-ord('a')] += 1
        for i in range(26):
            if ran[i] > mag[i]:
                return False
        return True 