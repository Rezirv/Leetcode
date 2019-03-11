class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        last = [[1]]
        numRows -= 1
        while numRows:
            last.append([1]+[a+b for a,b in zip(last[-1][:-1], last[-1][1:])] + [1])
            numRows -= 1
        return last