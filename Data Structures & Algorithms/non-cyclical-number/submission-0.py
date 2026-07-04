class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        def sod(m):
            su=0
            while(m>0):
                r=m%10
                su+=r*r
                m=m//10
            return su
        while n!=1 and n not in s:
            s.add(n)
            n=sod(n)
        return n==1
        