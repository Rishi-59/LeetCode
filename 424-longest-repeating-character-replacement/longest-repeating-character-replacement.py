class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        max_f = 0
        max_l = 0
        l,r = 0, 0
            
        while r < len(s):
            freq[s[r]] += 1
            max_f = max(freq[s[r]],max_f)
            changes = r-l + 1 - max_f
            if changes > k :
                freq[s[l]] -= 1
                l += 1

            if changes <= k:
                max_l = max(max_l,r-l+1)
            r += 1

        return max_l

            