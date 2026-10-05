class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = int((1 + n) * n / 2)
        for i in nums:
            Sum -= i
        return Sum