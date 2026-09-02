class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        items=[]
        for i in range(len(val)):
            ratio=val[i]/wt[i]
            items.append((ratio,val[i],wt[i]))
        profit=0.0
        items.sort(reverse=True)
        for ratio,value,weight in items:
            if weight<=cap:
                profit+=value
                cap-=weight
            else:
                profit+=value*(cap/weight)
                break
        return profit
