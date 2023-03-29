class Solution:
    d= {
        '2': ('a','b','c'),
        '3': ('d','e','f'),
        '4': ('g','h','i'),
        '5': ('j','k','l'),
        '6': ('m','n','o'),
        '7': ('p','q','r','s'),
        '8': ('t','u','v'),
        '9': ('w','x','y','z'),
        
    }

    def toCombine(self, digits):
        pass

    def letterCombinationsHelper(self, digits: str, lstStr:list):
        for letter in self.d.get(digit):
            comb.append()
            
    
    def letterCombinations2(self, digits: str) -> list[str]:
        lst_str = list()
        if i==len(digits)-1:
            for item in self.d.get(digits[i]):
                lst_str.append(item)
            
            for i in range(len(digits)-1, -1,-1 ):
                for item in self.d.get(digits[i]):
                    for j in lst_str:
                        lst_str.
                
                



    def letterCombinations(self, digits: str) -> list[str]:
        
        while i< len(digits):

        
        s_lst=list()
        digits= str(digits)
        if len(digits)==0:
            return []
        
        



        

        for l1 in (self.d.get(digits[0])) :
            for l2 in self.d.get(digits[1]):
                for l3 in self.d.get(digits[2]):
                    for l4 in self.d.get(digits[3]):
                        comb = l1+l2+l3+l4
                        s_lst.append(comb)
        return s_lst

s= Solution()
digits= 23
print( s.letterCombinations(digits))
