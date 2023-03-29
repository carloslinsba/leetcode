# [15:59, 03/10/2022] Felipe Frechiani:  outro era dado uma lista de strings
# [16:00, 03/10/2022] Felipe Frechiani: [red2, green4, black1] ordenar pelo número e apresentar sem ter esse numero

import re

class Solution:

    def letter(self, input:list[str])-> list[str]:
        pd= '\d+$'
        ps = '\A\D+'
        d = dict()
        lst_digits= list()
        for item in input:
            digits = re.search(pd, item)
            word = re.search(ps, item)
            #print (digits.group())
            #print (word.group())
            d[int(digits.group())] = word.group()
            lst_digits.append(int(digits.group()))
        
        lst_digits.sort()
        lst_answer = list()
        for item in lst_digits:
            lst_answer.append(d[item])
        print (lst_digits)
        print (lst_answer)

        
            





s= Solution()
input = ['red2', 'green4', 'black1', 'gray8', 'blue9', 'yellow24']  
s.letter(input)