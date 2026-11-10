class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        total = 0
        min_len = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_len = min(r-l+1,min_len)
                total -= nums[l]
                l += 1
                
            
        return min_len if min_len != float('inf') else 0
        