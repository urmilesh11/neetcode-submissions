class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        for j in t:
            if j in f:
                f[j]-=1
            else:
                return False
        for v in f.values():
            if v!=0:
                return False
        return True
        
        