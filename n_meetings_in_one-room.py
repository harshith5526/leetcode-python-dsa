class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        count=0
        n=len(start)
        lastend=-1

        for i in range(n):
            if start[i]>lastend:
                count+=1
                lastend=end[i]
        return count
