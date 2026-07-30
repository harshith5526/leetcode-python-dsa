class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        low=0
        high=len(nums)-1
        def merge(low,mid,high):
            i=low
            j=mid+1
            temp=[]
            while(i<=mid and j<=high):
                if(nums[i]<=nums[j]):
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1

            while(i<=mid):
                temp.append(nums[i])
                i+=1
            while(j<=high):
                temp.append(nums[j])
                j+=1
            
            for i in range(low,high+1):
                nums[i]=temp[i-low]

        def counting(low,mid,high):
            count=0
            j=mid+1
            for i in range(low,mid+1):
                while j<=high and nums[i]>2*nums[j]:
                    j+=1
                count+=j-(mid+1)
            return count
            

        
        def sort(low,high):
            if(low>=high):
                return 0
            mid=(low+high)//2
            count=0
            count+=sort(low,mid)
            count+=sort(mid+1,high)
            count+=counting(low,mid,high)
            merge(low,mid,high)
            return count
        return sort(0,len(nums)-1)
