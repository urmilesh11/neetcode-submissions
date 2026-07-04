class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ts=n*(n+1)//2
        if ts==sum(nums):
            return 0
        return abs(ts-sum(nums))
        