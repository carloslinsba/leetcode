class Solution:
    
    open = {
        "(" : ")",
        "{" : "}",
        "[" : "]",
    }

    def isValid(self, s: str) -> bool:
        l= len(s)
        if l%2!=0:
            return False
        if l==0:
            return True
        stack = []

        for item in s:
            if item in self.open.keys():
                stack.append(item)
                continue
            if not stack:
                return False
            if self.open.get(stack.pop()) != item:
                return False
        return  len(stack)==0

# ()[]{}
# ({()})

# for idx, item in enumerate(s):
        #     if idx >=l/2:
        #         return True
        #     if self.maps[item]!= s[l-idx-1]:
        #         return False
                

            




