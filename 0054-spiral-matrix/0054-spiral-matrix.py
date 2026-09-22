class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def transpose(m):
            r = len(m)
            c = len(m[0])
            t = []
            for j in range(c):
                new_row = []
                for i in range(r):
                    new_row.append(m[i][j])
                t.append(new_row)
            return t
        n = len(matrix)
        m = len(matrix[0])
        lst = []
        while matrix:
            for i in matrix[0]:
                lst.append(i)
            matrix = matrix[1:]
            if matrix:
                matrix = transpose(matrix)
                matrix = matrix[::-1]
        return lst
        
