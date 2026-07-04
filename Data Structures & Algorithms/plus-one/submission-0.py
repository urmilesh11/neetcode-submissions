class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        c=1
        for i in range(l-1,-1,-1):
            digits[i]+=c
            if digits[i]<10:
                return digits
            digits[i]=0
        return [1]+digits
        