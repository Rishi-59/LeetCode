class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0 , len(height) - 1
        m_area = 0
        while l < r :
            area = (r - l )* min(height[l],height[r])
            m_area = max(m_area , area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m_area