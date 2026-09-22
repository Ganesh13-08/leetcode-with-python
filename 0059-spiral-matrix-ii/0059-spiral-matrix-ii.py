class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[0]*n for _ in range(n)]
        num = 1
        for x in range((n+1)//2):

            for i in range(x,n-x):
                res[x][i] = num
                num+=1
            
            for i in range(x+1,n-x):
                res[i][n-x-1] = num
                num+=1

            for i in range(n-x-2,x-1,-1):
                res[n-x-1][i] = num
                num+=1
            
            for i in range(n-x-2,x,-1):
                res[i][x] = num
                num+=1
            
        return res
