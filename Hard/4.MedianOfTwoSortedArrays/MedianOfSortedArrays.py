class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2!=0:
            return nums1[int(len(nums1)/2)]
        add1= nums1[int(len(nums1)/2-1)]
        add2= nums1[(int(len(nums1)/2))]
        return (add1+add2)/2



s= Solution()
nums1 = [1,2]
nums2 = [3,4]
print (s.findMedianSortedArrays(nums1, nums2))