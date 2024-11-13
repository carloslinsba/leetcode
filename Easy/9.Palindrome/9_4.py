class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        l = len(s)
        i=0
        while i< l-1-i:
            if s[i]!=s[l-1-i]:
                return False
            i+=1
        return True
            

            

