class Solution:
    def rotate(self, matrix):
     
        nums=len(matrix)
        for i in range(nums):
            for j in range(i,nums):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(nums):
            matrix[i]=list(reversed(matrix[i]))
