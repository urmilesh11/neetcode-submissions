class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f={}
        ans=[-1]*2
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem not in f:
                f[nums[i]]=i
            else:
                ans[0]=f[rem]
                ans[1]=i
        return ans


        