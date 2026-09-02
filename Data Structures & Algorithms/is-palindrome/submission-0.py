import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        _PUNCT_TABLE = str.maketrans('', '', string.punctuation)

        s = s.replace(" ", "").lower().translate(_PUNCT_TABLE)
        print(s)
        n = len(s)
        i, j = 0, n - 1

        while (i<=j):
            if s[i] != s[j]:
                return False
            i +=1
            j -= 1
        else:
            return True
        