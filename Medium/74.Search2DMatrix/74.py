class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #naive1
        i=0
        while True:
            if i>=len(matrix):
                return False
            if target>matrix[i][len(matrix[i])-1]:
                i+=1
                continue
            else:
                if target in matrix[i]:
                    return True
                return False
            
