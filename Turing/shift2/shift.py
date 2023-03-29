# [15:57, 03/10/2022] Felipe Frechiani: Sim, fazer um shift de uma lista em n números.
# [15:58, 03/10/2022] Felipe Frechiani: [1,2,3,4] shift de 2 vira [3,4,12]



class Solution:
    def shift(self, input:list[int])-> list[int]:
        
        print (input)
        if len(input)<2:
            return input
        first = input.pop(0)
        second = input.pop(0)

        input.append(first)
        input.append(second)

        print (input)






s=Solution()
#input = [1,2,3,4,20,30,898789,-765]
input = [1,2,3]
s.shift(input)