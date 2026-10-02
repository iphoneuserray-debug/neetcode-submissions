class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cMin, cMax = 1, 1

        for i in range(len(nums)):
            tmp = cMax * nums[i]
            cMax = max(cMin * nums[i], nums[i], nums[i] * cMax)
            cMin = min(nums[i], tmp, nums[i] * cMin)
            res = max(res, cMax)
        return res