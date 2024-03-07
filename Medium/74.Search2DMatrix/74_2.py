class Solution:
    def searchMatrixHelper(self, matrix: List[List[int]], target: int) -> bool:
        pass
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #naive1
        i=int(len(matrix)/2)
        while True:
            if i>=len(matrix):
                return False
            if target>matrix[i][len(matrix[i])-1]:
                self.searchMatrix(matrix[i:], target)
                continue
            else:
                self.searchMatrix(matrix[:i], target)
                if target in matrix[i]:
                    return True
                return False
            
