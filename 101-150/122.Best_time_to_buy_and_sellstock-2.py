class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxprofit=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit=prices[i]-prices[i-1]
                maxprofit=maxprofit+profit
        return maxprofit
