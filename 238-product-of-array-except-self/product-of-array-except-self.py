class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1]
        r_prod = 1
        n = len(nums)
        
    
        for i in range(1,n):
            ans.append(ans[i-1]*nums[i-1])
        
        for i in range(n-1,-1,-1):
            ans[i] *= r_prod
            r_prod *= nums[i]

        return ans

