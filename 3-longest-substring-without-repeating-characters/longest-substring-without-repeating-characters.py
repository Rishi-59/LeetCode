class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = r = 0
        max_l = 0
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                max_l = max(max_l,r-l+1)
                r += 1
            else:
                visited.remove(s[l])
                l += 1
        return max_l

            
