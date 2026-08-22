class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        sum=0
        product=1
        while temp>0:
            digit=temp%10
            sum+=digit
            product*=digit
            temp//=10
        total=sum+product
        if n%total==0:
            return True
        else:
            return False
        
