class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        i,j = 0,0
        trans = [[0 for _ in range(r)]for _ in range(c)] 
        while i!=r:
            j=0
            while j!=c:
                trans[i][j] = matrix[j][i]
                j+=1
            i+=1
        for i in range(r):
            for j in range(c):
                matrix[i][j] = trans[i][j]
        for i in matrix:
            i.reverse()