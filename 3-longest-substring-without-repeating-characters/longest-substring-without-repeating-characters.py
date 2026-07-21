class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        visited = set()
        max_unique = 0

        while right < len(s):
            while right < len(s) and s[right] not in visited:
                visited.add(s[right])
                right += 1

            max_unique = max(max_unique, right - left)

            while right < len(s) and s[right] in visited:
                visited.remove(s[left])
                left += 1

        return max_unique