class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_f = 0
        ans = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1

            if max_f < freq[s[r]]:
                max_f = freq[s[r]]
            
            if (r-l+1) - max_f > k:
                freq[s[l]] -= 1
                l += 1
            
            if ans < (r-l+1):
                ans = (r-l+1)
            
        return ans