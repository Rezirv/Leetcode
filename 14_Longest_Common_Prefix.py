class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            flag = 0
            break_flag = False
            min_num = len(min(strs, key=len))
            for i in range(min_num):
                for j in range(len(strs) - 1):
                    if (strs[j][i] != strs[j + 1][i]):
                        break_flag = True
                        break
                if break_flag == False:
                    flag += 1
                else:
                    break
            return strs[0][:flag]

