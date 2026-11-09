class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n 

        p = 1
        for i in range(1,n):
            p *= nums[i-1]
            ans[i] *= p
        
        s = 1
        for i in range(n-1,-1,-1):
            ans[i] *= s
            s *= nums[i]

        return ans

