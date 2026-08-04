class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1],[1,1]]
        if numRows == 1:
            return tri[:1]
        if numRows == 2:
            return tri
        
        while len(tri) < numRows:
            ans = [1]
            ref = tri[-1]
            for i in range(len(ref)-1):
                j = i + 1 
                ans.append(ref[i]+ref[j])
            ans.append(1)
            tri.append(ans)

        return tri
            