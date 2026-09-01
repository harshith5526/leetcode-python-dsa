class Solution:
    def JobScheduling(self, Jobs):
        #your code goes here
        Jobs.sort(key=lambda x:x[2],reverse=True)
        maxdeadline=0
        for job in Jobs:
            maxdeadline=max(maxdeadline,job[1])
        slot=[-1]*(maxdeadline+1)
        count=0
        profit=0
        for job in Jobs:
            for j in range(job[1],0,-1):
                if slot[j]==-1:
                    slot[j]=job[0]
                    count+=1
                    profit+=job[2]
                    break
        return [count,profit]
