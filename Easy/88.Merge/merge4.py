class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i,num in enumerate(nums2):
            nums1.pop(n+m-1-i)
            nums1.append(num)
        nums1.sort()
        
        print(nums1)
        return

s= Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s.merge(nums1, m, nums2, n)
