class Solution:
    def merge(self, intervals):
        n=len(intervals)
        intervals=sorted(intervals)
        current_start,current_end=intervals[0]
        ans=[]

        for i in range(1,n):
            next_start,next_end=intervals[i]
            if next_start<=current_end:
                current_end=max(current_end,next_end)
            else:
                ans.append([current_start,current_end])
                current_start,current_end=next_start,next_end
        ans.append([current_start,current_end])
        return ans
