class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        nums1 = {}
        nums2 = {}
        for i in s:
            if i in nums1:
                nums1[i] += 1
            else:
                nums1[i] = 1
        for i in t:
            if i in nums2:
                nums2[i] += 1
            else:
                nums2[i] = 1
        for key, value in nums2.items():
            if key not in nums1:
                return key
            elif value > nums1[key]:
                return key