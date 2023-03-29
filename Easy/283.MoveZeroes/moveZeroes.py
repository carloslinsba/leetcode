class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lstzeroes = []
        for index, item in enumerate(nums):
            if item == 0:
                lstzeroes.insert(0, index)
        for item in lstzeroes:
            nums.pop(item)
            nums.append(0)



        """
        Do not return anything, modify nums in-place instead.
        """