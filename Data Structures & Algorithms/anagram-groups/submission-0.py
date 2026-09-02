class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arrs = []
        for i in range(len(strs)):
            arr = [0 for j in range(26)]
            for j in range(len(strs[i])):
                num = ord(strs[i][j]) - ord('a')
                arr[num] += 1
            arrs.append(arr)
        
        index_arr = {}
        for i in range(len(strs)):
            tp = tuple(arrs[i])
            if (index_arr.get(tp) != None):
                index_arr[tp].append(i)
            else:
                index_arr[tp] = [i]
        
        result = []
        for value in index_arr.values():
            re = []
            for i in range(len(value)):
                re.append(strs[value[i]])
            result.append(re)
        return result