class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            flag=False
            for j in range(m):
                if mat[i][j]==0:
                    flag=True
                    break
            if flag:
                for j in range(m):
                    if mat[i][j]!=0:
                        mat[i][j]=math.inf
        for j in range(m):
            flag=False
            for i in range(n):
                if mat[i][j]==0:
                    flag=True
                    break
            if flag:
                for i in range(n):
                    if mat[i][j]!=0:
                        mat[i][j]=math.inf
        for i in range(n):
            for j in range(m):
                if mat[i][j] == math.inf:
                    mat[i][j]=0
        
                            
        