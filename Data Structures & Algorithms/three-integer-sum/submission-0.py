class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        n = len(nums)
        nums.sort()
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            
        result = []

        for i in range(len(nums)):
            
            hashmap[nums[i]] -= 1
            if i and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                hashmap[nums[j]] -= 1
                if j > (i + 1) and nums[j - 1] == nums[j]:
                    continue
                s = nums[i] + nums[j]
                target = 0 - s
                h = hashmap.get(target)
                
                if h != None:
                    if (hashmap[target] > 0):
                        result.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                hashmap[nums[j]] += 1
         
        return result
