class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=='':
            return 0
        else:
            strs = s.split(' ')
            if len(set(strs)) == 1 and (list(set(strs))[0]=='')  :
                return 0
            else:
                i = -1
                while strs[i] =='':
                    i -=1
                return len(strs[i])