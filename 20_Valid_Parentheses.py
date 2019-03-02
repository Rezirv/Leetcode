class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if len(s) % 2 != 0:
            return False
        elif len(s) == 0:
            return True
        else:
            stack = []
            for i in s:
                if i in dict:
                    stack.append(i)
                else:
                    if len(stack) == 0:
                        return False
                    a = stack.pop()
                    if dict[a] == i:
                        continue
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False



