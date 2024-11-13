class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 0
        currentString=""
        newString = ""
        for char in s:
            if char in currentString:
                partitions+=1
                newString= ""
                currentString=""
            newString += char
            currentString+=char
        if newString!= "":
            partitions+=1

        return partitions


        