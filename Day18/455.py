class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=0
        r=0
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        while l<m and r<n:
            if g[r]<=s[l]:
                r+=1    
            l+=1
        return r
        