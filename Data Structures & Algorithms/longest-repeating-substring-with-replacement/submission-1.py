from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        
        i, j = 0, 0
        hp = defaultdict(int)

        while j < len(s):
            hp[s[j]] += 1
            while ((j - i + 1) - max(hp.values())) > k:
                hp[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)
            j += 1
        
        return longest
                    


        