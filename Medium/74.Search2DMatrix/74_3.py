#naive approach
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target>matrix[i][0] and target>matrix[i][len(matrix[i])-1]:
                continue
            for j in range(len(matrix[i])):
                if target == matrix[i][j]:
                    return True
                if target < matrix[i][j]:
                    return False
        return False
        


#done