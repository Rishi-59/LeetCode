class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return

        i = 0
        while True:
            if nums[i] == 0:
                break
            i += 1

        for j in range(i,len(nums)):
            if nums[j] != 0 :
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1 
            j += 1
        
        return
