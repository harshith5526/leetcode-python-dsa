class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ans=0
        map=set()
        for right in range(len(s)):
            while s[right] in map:
                map.remove(s[left])
                left+=1
            map.add(s[right])
            ans=max(ans,right-left+1)
        return ans
      
