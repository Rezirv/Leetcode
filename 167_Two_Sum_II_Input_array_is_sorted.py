class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        p = 0
        q = length - 1
        while p != q:
            if target > numbers[p] + numbers[q]:
                p += 1
            elif target < numbers[p] + numbers[q]:
                q -= 1
            else:
                return [p + 1, q + 1]
