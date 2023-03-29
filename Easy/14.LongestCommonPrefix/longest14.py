class Solution:

    def isLetterinAllWords(self,strs, letter, position):
        try:
            for word in strs:
                    if letter == word[position]:
                        continue
                    else:
                        return False
            return True
        except: 
            return False
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        # go into the first word
        #state if 1st(i) letter is in all other words at the same position
        #replace (i) with i+
        if len(strs)<=0:
            return ""
        
        i=0
        initialWord = strs[0]
        for letter in initialWord:
            if self.isLetterinAllWords(strs, letter, i):
                i+=1
            else:
                break
        return initialWord[0:i]

    
     
     
    


        
        
        
            
            


         
   