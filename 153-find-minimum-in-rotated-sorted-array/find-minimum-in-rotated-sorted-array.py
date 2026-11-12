class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0 , len(nums)-1
        ans = float('inf')
        while l <= r:
            m = (l+r) // 2

            if nums[l] <= nums[m]:
                ans = min(nums[l],ans)
                l = m + 1
            else:
                r = m - 1
                ans = min(nums[m],ans)
        
        return ans