class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        lines =[""]*numRows
        
        if numRows ==2:
            i=0
            for letter in s:
                lines[i%2]+=letter
                i+=1
        else:

            row=0
            rowIndex = numRows-1
            printLetter = False

            for letter in s:
                if printLetter:
                    lines[rowIndex]+=letter
                    if rowIndex-1 == 0:
                        rowIndex = numRows-1
                        printLetter = False
                    else:
                        rowIndex-=1
                    continue

                lines[row] +=letter
                row+=1
                if row==numRows:
                    rowIndex-=1
                    row=0
                    printLetter= True
        
        ret = ""
        ret = ret.join(lines)
        return ret


s = "PAYPALISHIRING"
numRows = 2
sol = Solution()
print (sol.convert(s,numRows))





            



