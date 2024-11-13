class Solution:
    
    def simplifyPath(self, path: str) -> str:
        
        path_stack = []
        l = path.split("/")
        for item in l:
            if item =="" or item =="/" or item==".":
                continue
            if item == "..":
                if path_stack:
                    path_stack.pop()
                continue
            path_stack.append(item)
            
        final_string = "/"
        for item in path_stack:
            final_string+= item 
            final_string+= "/"
        
        final_string = final_string.removesuffix("/")

        if final_string:
            return final_string
        else:
            return "/"


s = Solution()
# input = ".."
# input = "/home/../foo/.."
input = "/home/user/Documents/../Pictures"
print(s.simplifyPath(input))

#solve root


        

        
        