class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while True:
            try: 
                nums.remove(val)
            except:
                return
        

s = Solution()
nums = [3,2,2,3]
val = 3
s.removeElement(nums, val)