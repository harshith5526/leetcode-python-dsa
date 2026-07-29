class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[ 0 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    up=dp[i-1][j]
                    left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]
