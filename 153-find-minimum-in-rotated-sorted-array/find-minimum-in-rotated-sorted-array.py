class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l , r = 0 , len(nums) - 1

        ans = float('inf')

        while l <= r:
            m = l + (r - l) // 2

            if nums[l] <= nums[m]:
                ans = min(nums[l], ans)
                l = m + 1
            else:
                ans = min(nums[m], ans)
                r = m - 1
        
        return ans

            
                
