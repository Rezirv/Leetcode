class Solution:
    def reverseVowels(self, s: str) -> str:
        p = 0
        s = list(s)
        q = len(s)-1
        y = ['a','e','i','o','u','A','E','I','O','U']
        while p<=q:
            if s[p] not in y and s[q] not in y:
                p += 1
                q -= 1
            elif s[p] in y and s[q] not in y:
                q -= 1
            elif s[p] not in y and s[q] in y:
                p += 1
            else:
                flag = s[p]
                s[p] = s[q]
                s[q] = flag
                p += 1
                q -= 1
        return ''.join(s)