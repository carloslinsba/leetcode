class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        prior =None
        for item in nums:
            if item == prior:
                return True
            prior = item
        return False

