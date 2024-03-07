class Solution:
    def canReach(self, idx, nums:list[int])->bool:
        pass    
    
    def latestThatCanReach(self,nums:list[int])->int:
        for idx,item in enumerate(nums):
            if item >= len(nums)-1-idx:
                return idx



    
    def jump(self, nums: list[int]) -> int:
        #naive solution  15:08
        #see which one is the latest that can reach.
        #after that, go to that index and redo it until index 0 is found.
        jumps=0
        current_idx=len(nums)-1
        if current_idx==0:
            return 0
        while True:
            current_idx= self.latestThatCanReach(nums[:current_idx+1]) 
            jumps+=1
            if current_idx==0:
                return jumps
            nums=nums[:current_idx+1]


s= Solution()
nums = [2,3,1,1,4]    
s.jump(nums)



        