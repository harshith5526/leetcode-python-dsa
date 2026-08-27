class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        array=[]
        for i in range(len(start)):
            array.append((end[i],start[i]))

        count=0
        lastend=-1
        for endtime,starttime in array:
            if starttime>lastend:
                count+=1
                lastend=endtime
        return count
