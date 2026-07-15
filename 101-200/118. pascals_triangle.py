class Solution:
    def generate(self, numRows)
        pascal=[]
        for row in range(numRows):
            current=[1]*(row+1)
            for col in range(1,row):
                current[col]=pascal[row-1][col-1]+pascal[row-1][col]
            pascal.append(current)
        return pascal

        
