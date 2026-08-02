class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [row[:] for row in matrix]
        
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = ans[i][j]

        return