class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        hp = {}

        i, j = 0, 0
        while j < len(s):
            val = hp.get(s[j])
            if val == None:
                hp[s[j]] = True
                length = j - i + 1
                longest = max(longest, length)
                j += 1
            else:
                st = s[i : j]
                print(st)
                k = st.index(s[j])
                for d in range(i, i + k + 1):
                    del hp[s[d]]
                i = i + k + 1
            
        return longest