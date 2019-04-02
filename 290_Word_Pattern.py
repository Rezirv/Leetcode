class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p_dict ={}
        str_list = str.split(' ')
        if len(pattern)!=len(str_list):
            return False
        for i,j in zip(pattern,str_list):
            if i not in p_dict:
                p_dict[i] = j
            elif i in p_dict and p_dict[i]!=j:
                return False
        if len(set(p_dict.values()))!=len(p_dict.values()):
            return False
        else:
            return True