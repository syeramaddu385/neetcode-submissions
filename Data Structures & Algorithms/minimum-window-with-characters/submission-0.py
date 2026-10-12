class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        have = 0
        tMap = {}
        windowMap = {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        res, resLen = [-1, -1], float("inf")

        for r in range (len(s)):
            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)

            if s[r] in tMap and windowMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == len(tMap):
                if  (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                if s[l] in tMap and windowMap[s[l]] == tMap[s[l]]:
                    have -= 1
                windowMap[s[l]] -= 1
                l += 1
        
        l, r = res

        return s[l : r + 1] if resLen != float("inf") else ""