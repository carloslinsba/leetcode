class Solution:
    #naive approach
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer =[]
        temp =[]
        for i, temperature in enumerate(temperatures):
            temp.append ((temperature, i))
        temp = list(set(temp))
        temp.sort()
        for i in range(len(temperatures)):
            mini=len(temperatures)
            for j in range(temp.index(temperatures[i])+1, len(temp)):
                a,b=temp[j]
                if b<mini:
                    mini=b
            answer[i]=mini-i
        
        return answer

#not done

#naive
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         answer =[]
#         for i in range(len(temperatures)):
#             answer.append(0)
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[i]<temperatures[j]:
#                     answer[i]= (j-i)
#                     break
#         return answer
        