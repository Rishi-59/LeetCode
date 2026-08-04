class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        
        for row in range(numRows):
            ans = [1] * (row + 1)
            for i in range(1,row):
                ans[i] = tri[row-1][i] + tri[row-1][i-1]
            tri.append(ans)

        return tri
            