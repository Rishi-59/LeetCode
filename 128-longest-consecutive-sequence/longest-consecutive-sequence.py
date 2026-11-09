class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                ct = 1

                while i+ct in nums:
                    ct+=1
                    
                l = max(ct,l)
        return l