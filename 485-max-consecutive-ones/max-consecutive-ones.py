class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                max_c = max(max_c,count)
                count = 0
        
        return max(max_c,count)