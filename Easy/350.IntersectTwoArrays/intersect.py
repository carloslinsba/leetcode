class Solution:

    def helper(self, d1:dict, d2:dict)-> list[int]:
        lstintersect=[]
        for item in d1:
            if d2.get(item):
                if d1[item] < d2[item]:
                    n=d1[item]
                else:
                    n=d2[item]
                for i in range (0, n):
                    lstintersect.append(item)
        return lstintersect

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d1=dict()
        d2=dict()
        if len(nums1)==0 or len(nums2)==0:
            return []
        
        for item in nums1:
            if d1.get(item):
                d1[item]+=1
            else:
                d1[item]=1

        for item in nums2:
            if d2.get(item):
                d2[item]+=1
            else:
                d2[item]=1
        if len(d1)< len(d2):
            return self.helper(d1, d2)
        else:
            return self.helper(d2, d1)

s= Solution()
#nums1 = [1,2,2,1]
#nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print ( s.intersect(nums1, nums2)) 

