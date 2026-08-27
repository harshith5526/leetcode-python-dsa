class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        Arrival.sort()
        Departure.sort()
        i=0
        j=0
        platforms=0
        answer=0
        while (i<len(Arrival)) and (j<len(Departure)):
            if Arrival[i]<=Departure[j]:
                platforms+=1
                answer=max(answer,platforms)
                i+=1
            else:
                platforms-=1
                j+=1
        return answer
