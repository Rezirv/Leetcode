class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #反向思考题意，n-1个数同时加1，即1一个数减1，所以只能减到最小的数为止
        minnum = min(nums)
        res = 0
        for i in nums:
            res += (i - minnum)
        return res