class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        bp = None

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                bp = i
                break
        
        if bp == None:
            return nums.reverse()

        for i in range(n-1,-1,-1):
            if nums[i] > nums[bp]:
                nums[i] , nums[bp] = nums[bp] , nums[i]
                break
        
        l = bp + 1
        r = n - 1
        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1
        
        return