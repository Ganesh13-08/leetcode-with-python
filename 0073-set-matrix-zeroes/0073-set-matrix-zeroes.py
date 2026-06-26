class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        lst = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    lst.append((r,c))
        for r,c in lst:
            for i in range(n):
                matrix[r][i]=0
            for i in range(m):
                matrix[i][c]=0
            
                    