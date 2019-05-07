class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res
        hash_p = 0
        hash_s = 0
        for i in range(len(p)):
            hash_p += hash(p[i])
            hash_s += hash(s[i])
        if hash_p == hash_s:
            res.append(0)
        for i in range(len(p), len(s)):
            hash_s += hash(s[i]) - hash(s[i-len(p)])
            if hash_s == hash_p:
                res.append(i-len(p)+1)
        return res