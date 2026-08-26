class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones=[]
        for i in range(len(s)):
            if s[i]=='1':
                ones.append(i)
        if len(ones)<k:
            return ""
        ans=""
        min_len=float('inf')
        for i in range(len(ones)-k+1):
            start=ones[i]
            end=ones[i+k-1]
            length=end-start+1
            sub=s[start:end+1]
            if length<min_len:
                min_len=length
                ans=sub
            elif length==min_len:
                ans=min(ans,sub)
        return ans
