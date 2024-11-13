class Solution:
    
    def isHappy(self,n: int) -> bool:
        d = dict()

        def isHappyHelper(n: int) -> bool:
            s = str(n)
            summ=0
            for char in s:
                n=int(char)
                summ+=n*n
            if summ==1:
                return True
            if d.get(summ):
                return False
            d[summ] = True
            return isHappyHelper(summ)
        return isHappyHelper(n)
        
        