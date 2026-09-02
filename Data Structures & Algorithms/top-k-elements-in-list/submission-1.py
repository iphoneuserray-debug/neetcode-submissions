class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            num = count.get(nums[i])
            if num == None:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        freq_bucket = [[] for i in range(len(nums))]
        for key, value in count.items():
            freq_bucket[value - 1].append(key)
        result = []
        for i in range(len(freq_bucket) - 1, -1, -1):
            for j in range(len(freq_bucket[i])):
                if (len(result) >= k):
                    break
                result.append(freq_bucket[i][j])
        return result