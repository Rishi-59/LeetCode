class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def rotate1():
           
        #     temp = nums[-1]

        #     for i in range(len(nums)-1,0,-1):
        #         nums[i] = nums[i-1]

        #     nums[0] = temp

        # for _ in range(k):
        #     rotate1()
        k %= len(nums) 
        if len(nums) < 2 or k==0:
            return nums
        fwd = nums[-k:]
        last = nums[:len(nums)-k]
        nums[:] = fwd + last

        