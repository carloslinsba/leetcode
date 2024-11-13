class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ndict= []
        for num in nums:
            if num in ndict:
                return num
            ndict.append(num)
        return -1