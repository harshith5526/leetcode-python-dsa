class Solution:
    def sumGame(self, num: str) -> bool:
        leftsum=0
        rightsum=0
        leftq=0
        rightq=0
        n=len(num)
        for i in range(n//2):
            if num[i]=='?':
                leftq+=1
            else:
                leftsum+=int(num[i])
        for i in range(n//2,n):
            if num[i]=='?':
                rightq+=1
            else:
                rightsum+=int(num[i])
        if (leftq+rightq)%2==1:
            return True
        return (leftsum-rightsum)!=9*(rightq-leftq)//2
