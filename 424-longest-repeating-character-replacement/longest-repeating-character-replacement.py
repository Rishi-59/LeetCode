class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_f = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if max_f < freq[s[r]]:
                max_f = freq[s[r]]

            w = r - l + 1
            changes = w - max_f
            if changes > k:
                freq[s[l]] -= 1
                l += 1

            elif ans < w:
                ans = w

        return ans
