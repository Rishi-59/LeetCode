class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2 :
            return True

        miss = 0

        for i in range(1,n):
            if nums[i] < nums[i-1] and miss:
                return False
            if nums[i] < nums[i-1] and not miss:
                miss = 1
                if nums[-1] > nums[0]:
                    return False
        
        return True
