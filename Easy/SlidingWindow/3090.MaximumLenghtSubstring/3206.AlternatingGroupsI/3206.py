class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        result=0
        for i in range (0,len(colors)):
            if colors[i-2]==colors[i] and colors[i-1]!=colors[i]:
                result+=1
        return result


#time complexity: O(n)
#space complexity: O(1)