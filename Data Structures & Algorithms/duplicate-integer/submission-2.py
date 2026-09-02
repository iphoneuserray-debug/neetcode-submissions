class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = {}
        for i in range(len(nums)):
            if (arr.get(nums[i]) == False):
                return True
            else:
                arr[nums[i]] = False
        return False