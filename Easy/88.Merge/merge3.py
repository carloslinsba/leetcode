class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            nums1=nums2
            return
        if n==0:
            return
        while (i<n+m and j<n):
            if nums1[i] <= nums2[j]:
                nums1.insert(nums2[j])
                j+=1
            i+=1
        if j<n:
            toInsert= n-j
            



            
        