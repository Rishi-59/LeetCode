class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0 , len(nums)-1
        while l <= r:
            m = (l+r) // 2

            if l == r:
                return nums[l]

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1