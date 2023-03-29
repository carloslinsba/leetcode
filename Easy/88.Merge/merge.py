class Solution:
    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #15:36
        inums1=0
        jnums2=0
        newArray=[]

        if n==0: 
            return
        if m==0:
            for item in nums2:
                nums1.pop()
                nums1.append(item)
            return
            

        for i in range(n+m): 
            if nums1[inums1]>nums2[jnums2] or inums1>=m:
                newArray.append(nums2[jnums2])
                jnums2+=1
            else:
                newArray.append(nums1[inums1])
                inums1+=1
        nums1 = newArray


    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #15:59
        inums1=0
        jnums2=0

        if n==0: 
            return
        if m==0:
            for index,item in enumerate(nums2):
                nums1[index]= item
            return
        newArray=[]

        for i in range(n+m): 
            if jnums2>=n:
                newArray.append(nums1[inums1])
                inums1+=1
                continue
            if nums1[inums1]<=nums2[jnums2] and inums1<m:
                newArray.append(nums1[inums1])
                inums1+=1
            else:
                newArray.append(nums2[jnums2])
                jnums2+=1
                continue
        for index,item in enumerate(newArray):
            nums1[index]= item

        
"""     def merge3(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #edge cases empty arrays
        if n==0:
            return
        if m==0:
            for item in nums2:
                nums1.pop(0)
                nums1.append(item)
            return   

        i=0
        j=0
        controli=0


        for item in range (n+m):        
            if i>=m:
                nums1.pop(n+m-1)
                nums1.insert(i, nums2[j])
                i+=1
                j+=1
                continue
            if j>=n:
                return
            if nums1[i]<=nums2[j]:
                i+=1
                continue
            else:
                nums1.pop(n+m-1)
                nums1.insert(i, nums2[j])
                j+=1
                #edge cases end of arrays
             """



            


        
s= Solution()
#nums1 = [4,5,6,0,0,0] 
#nums1 = [1,2,3,0,0,0] 
nums1 = [2,0] 
m = 1 
nums2 = [1] 
n = 1

s.merge(nums1, m, nums2, n)
print(nums1)



        