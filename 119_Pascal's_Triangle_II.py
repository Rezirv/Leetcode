class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last = [[1]]
        while rowIndex:
            last.append([1] + [a + b for a, b in zip(last[-1][:-1], last[-1][1:])] + [1])
            rowIndex -= 1
        return last[-1]

