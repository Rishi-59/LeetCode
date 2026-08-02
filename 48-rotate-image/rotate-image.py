class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Transpose
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
        # print(matrix)
        # Reverse each row
        for i in range(n):
            l,r = 0, n-1
            while l<=r:
                matrix[i][l] , matrix[i][r] = matrix[i][r] , matrix[i][l]
                l += 1
                r -= 1

        return
        
        #########################################

        # n = len(matrix)
        # ans = [row[:] for row in matrix]

        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][n - 1 - i] = ans[i][j]

        # return
