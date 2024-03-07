class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1count =0
        nums2count=0
        for i in range (0, m+n):
            if nums2count >=n:
                break
            if nums1count >=m+nums2count:
                nums1.insert(nums1count,nums2[nums2count])
                nums1count+=1
                nums2count+=1
                nums1.pop(len(nums1)-1)
                continue
            if nums1[nums1count] <=nums2[nums2count]:
                nums1count+=1
                continue
            else:
                nums1.insert(nums1count, nums2[nums2count])
                nums1count+=1
                nums2count+=1
                nums1.pop(len(nums1)-1)
        
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s.merge(nums1, m, nums2, n)


        