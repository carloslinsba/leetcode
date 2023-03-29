class Solution:

    def findLuckyNumber(self, arr:list[int]):
        #edge cases
        if len(arr)<1:
            return -1


        arr.sort(reverse=True)
        i=0
        lastItem= None
        for item in arr:
            if item ==lastItem:
                i+=1
                if i+1 ==item:
                    return item
            else:
                i=0
            lastItem=item
            if item==1:
                return item
        return -1

        
        pass


input = [0,2, 22, 241213,123,123,12,3,123,12,31,23,3]
s=Solution()
print (s.findLuckyNumber(input) )