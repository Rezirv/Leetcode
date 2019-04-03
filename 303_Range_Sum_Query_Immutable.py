class NumArray:

    def __init__(self, nums: List[int]):
        sum = 0
        tmp = [0]
        for i in range(len(nums)):
            sum += nums[i]
            tmp.append(sum)
        self.sumall = tmp

    def sumRange(self, i: int, j: int) -> int:
        return self.sumall[j + 1] - self.sumall[i]