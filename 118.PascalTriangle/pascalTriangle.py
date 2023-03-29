class Solution:
    #a fazer
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows ==0:
            return []
        if numRows <=2:
            return [1] if numRows==1 else [[1],[1,1]]
        pascal_list = []
        pascal_list.append([1])
        pascal_list.append([1,1])
        for i in range (2,numRows):
            new_list = []
            new_item
            for item in pascal_list[i-1]:


            pass



        