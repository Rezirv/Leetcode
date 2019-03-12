import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", '', s)
        slist = list(s.lower())
        clist = slist[:]
        slist.reverse()
        if clist == slist:
            return True
        else:
            return False