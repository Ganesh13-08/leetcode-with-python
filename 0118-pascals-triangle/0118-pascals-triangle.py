class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        m = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = m[i-1][j-1] + m[i-1][j]
            m.append(row)
        return m
            