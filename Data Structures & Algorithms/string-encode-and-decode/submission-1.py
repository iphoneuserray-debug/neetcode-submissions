class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        prefix = ""
        for s in strs:
            string += s
            prefix += str(len(s))
            prefix += ","
        prefix += "#"
        return prefix + string

    def decode(self, s: str) -> List[str]:
        result = []
        length = []
        lst = s.split("#", 1)
        numstring = lst[0].split(",")
        nums = [int(x) for x in numstring[:-1]]
        i = 0
        n = 0
        k = 0
        word = ""
        while (n < len(nums)):
            if nums[n] == 0:
                result.append("")
                n += 1
                continue
            if (i >= len(lst[1])) & nums[n] != 0:
                break
                
            word += lst[1][i]
            i += 1
            k += 1
            if k >= nums[n]:
                result.append(word)
                word = ""
                n += 1
                k = 0
        return result


                
            