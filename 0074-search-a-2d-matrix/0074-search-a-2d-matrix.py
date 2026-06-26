class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,0
        for i in range(m):
            if target>=matrix[i][j] and target<=matrix[i][n-1]:
                if target in matrix[i]:
                    return True
        return False

        