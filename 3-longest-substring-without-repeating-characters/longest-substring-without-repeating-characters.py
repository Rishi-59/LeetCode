class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            r+=1
            longest= max(longest, r-l)
        return longest

            
