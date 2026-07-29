class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        st = set(nums)

        for i in st:

            if i - 1 not in st:
                
                ct = 1
                x = i

                while x + 1 in st:
                    ct += 1
                    x += 1
                
                l = max(l,ct)
        
        return l