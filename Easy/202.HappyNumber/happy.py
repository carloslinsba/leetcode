class Solution:
    sumlist=[]
    def isHappyHelper(self, n:int)->bool:
        s = str(n)
        sum=0 
        for item in s:
            sum+= pow(int(item),2 )
        if sum == 1:
            return True
        
        if sum in self.sumlist:
            return False
        self.sumlist.append(sum)
        return self.isHappyHelper(sum)
    
    def isHappy(self, n:int)->bool:
        self.sumlist=[]
        return self.isHappyHelper(n)


        

s = Solution()
print( s.isHappy(23))