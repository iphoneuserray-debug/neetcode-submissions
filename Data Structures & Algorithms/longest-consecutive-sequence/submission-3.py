class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            h = hashmap.get(nums[i])
            if h == None:
                hashmap[nums[i]] = False
        
        head = {}
        for i in range(n):
            h = hashmap.get(nums[i] - 1)
            if h == None:
                head[nums[i]] = []
        
        max_count = 0
        for key in head.keys():
            num = key
            count = 0
            while hashmap.get(num + 1) != None:
                head[key].append(hashmap.get(num + 1))
                num += 1
                count += 1
            if count > max_count: 
                max_count = count
        return max_count + 1
        