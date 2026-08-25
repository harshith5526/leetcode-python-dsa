class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        path=[]
        def backtrack(ele):
            ans.append(path.copy())
            for i in range(ele,len(nums)):
                if i>ele and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
