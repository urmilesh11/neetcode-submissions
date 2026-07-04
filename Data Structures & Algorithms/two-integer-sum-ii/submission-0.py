class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=len(numbers)
        i=0
        j=l-1
        ans=[]
        while i<l and j>=0:
            if numbers[i]+numbers[j]==target:
                ans.append(i+1)
                ans.append(j+1)
                break
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1
        return ans

        