class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if (dic.get(s[i]) != None):
                dic[s[i]] = dic.get(s[i]) + 1
            else:
                dic[s[i]] = 1
        for i in range(len(t)):
            if dic.get(t[i]) == None:
                return False
            elif dic.get(t[i]) >= 1:
                dic[t[i]] = dic.get(t[i]) - 1
                if dic[t[i]] == 0:
                    del dic[t[i]]
            else:
                return False
        if (len(dic) > 0):
            return False
        return True
        