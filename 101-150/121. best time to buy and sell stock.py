class Solution:
    def maxProfit(self, prices):
        profit=0
        mini=prices[0]
        n=len(prices)
        for i in range(1,n):
            mini=min(prices[i],mini)
            profit=max(profit,prices[i]-mini)
        return profit
            
