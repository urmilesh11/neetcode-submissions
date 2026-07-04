class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=len(nums)
        lo=0
        hi=l-1
        if nums[lo]<=nums[hi] or l==1:
            return nums[lo]
        while(lo<=hi):
            mid=(lo+hi)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[lo]<=nums[mid]:
                lo=mid+1
            elif nums[mid]<=nums[hi]:
                hi=mid-1
        return -1

        