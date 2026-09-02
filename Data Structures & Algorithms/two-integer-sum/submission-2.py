class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hush = {}
        for i in range(len(nums)):
            if (hush.get(nums[i])==None):
                hush[nums[i]] = [i]
            else:
                hush[nums[i]].append(i)
        print(hush)
        for i in range(len(nums)):
            find = target-nums[i]
            if hush.get(find) == None:
                continue
            else:
                if (find == nums[i]) & (len(hush.get(find)) >= 2):
                    return [hush[find][0], hush[find][1]]
                elif find != nums[i]:
                    return [i, hush[find][0]]
