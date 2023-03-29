class Solution:
    def climbStairs(self, n: int) -> int:
        # i am at the n ->1
        # i am at n-1 -> 1
        #then, I am at (n-1)-1 = n-1 + n
        currentVal=0
        minusOneStep =0
        minusTwoSteps=0
        for i in range(n,-1, -1):
            if i==n:
                minusOneStep= 1
            if i==n-1:
                minusTwoSteps =1
            currentVal = minusOneStep + minusTwoSteps
            minusOneStep = minusTwoSteps
            minusTwoSteps = currentVal
        return currentVal



s = Solution()
n=5
print (s.climbStairs(n))

