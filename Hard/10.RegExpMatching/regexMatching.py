import re

class Solution:

    def regex_correcting(self,p:str)->str:
        p_adjust= p.split("*")
        was_equal= False

        
        if len(p_adjust)>1:
            for i in range(len(p_adjust)-1, 0, -1):
                if (p_adjust[i]== p_adjust[i-1]):
                    p_adjust.pop(i)
                    was_equal=True
                    continue
                else:
                    p_adjust[i]=p_adjust[i]+"*"
                    continue
                if was_equal:
                    p_adjust[i+1]= p_adjust[i+1]+"*"
                    was_equal=False
            if was_equal:
                    p_adjust[0]= p_adjust[0]+"*"
                    was_equal=False
                    
        new_p=''
        for item in p_adjust:
            new_p+=item
        
        return new_p



    def isMatch(self, s: str, p: str) -> bool:

        new_p = self.regex_correcting(p)
        pattern=re.compile('\A'+new_p+'\Z')
        x= re.search(pattern, s)
        return  True if x else False


sol= Solution()
s= "aaaaaaaaaaaaaaaaaaab"
p= "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
print (sol.isMatch(s, p)) 