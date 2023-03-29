class Solution:
    
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dict=dict()
        if not len(s)== len(t):
            return False
        new_word=""
        i=0
        for letter_s,letter_t in zip (s,t):
            if letter_s in iso_dict:
                new_word+=iso_dict.get(letter_s)
                if not iso_dict.get(letter_s) ==letter_t:
                    return False
            else:
                if letter_t in iso_dict.values():
                    return False
                iso_dict[letter_s] = letter_t
                new_word+=letter_t
            i+=1
        return True
        

        
            