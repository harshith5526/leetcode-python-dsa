class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=None
        ele2=None
        count1=0
        count2=0
        ans=[]
        n=len(nums)//3
        for num in nums:
            if num==ele1:
                count1+=1
            elif num==ele2:
                count2+=1
            elif count1==0:
                ele1=num
                count1=1
            elif count2==0:
                ele2=num
                count2=1  
            else:
                count1-=1
                count2-=1   
        count1=0
        count2=0
        for num in nums:
            if num==ele1:
                count1+=1
            elif num==ele2:
                count2+=1  
        if count1>n:
            ans.append(ele1)
        if count2>n:
            ans.append(ele2)
        return ans
