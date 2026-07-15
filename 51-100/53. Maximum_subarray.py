class Solution:
    def maxSubArray(self, nums):
            sum=0
            maxsum=nums[0]
            for num in nums:
                sum+=num
                if sum>maxsum:
                    maxsum=sum
                if sum<0:
                    sum=0
            return maxsum
