class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hp = {}
        for i in range(len(t)):
            hp[t[i]] = hp.get(t[i], 0) + 1

        l = 0
        min_len = 10000000
        res = ""
        for r in range(len(s)):

            if hp.get(s[r]) != None:
                hp[s[r]] -= 1
            
            while l <= r and max(hp.values()) <= 0:
                if (min_len > (r - l + 1)):
                    min_len = r - l + 1
                    res = s[l:r+1]
                
                if hp.get(s[l]) != None:
                    hp[s[l]] += 1
                l += 1
              
        return res