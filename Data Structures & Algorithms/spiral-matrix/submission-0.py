class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        n=len(mat)
        m=len(mat[0])
        i=j=0
        while n>1 and m>1:
            for k in range(1,m):
                ans.append(mat[i][j])
                j+=1
            for k in range(1,n):
                ans.append(mat[i][j])
                i+=1
            for k in range(1,m):
                ans.append(mat[i][j])
                j-=1
            for k in range(1,n):
                ans.append(mat[i][j])
                i-=1
            i+=1
            j+=1
            n-=2
            m-=2
        if n == 1:
            for k in range(m):
                ans.append(mat[i][j])
                j += 1
        elif m == 1:
            for k in range(n):
                ans.append(mat[i][j])
                i += 1
        return ans
        

        