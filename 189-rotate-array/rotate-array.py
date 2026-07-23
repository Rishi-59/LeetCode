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


        # k %= len(nums) 
        # nums[:] = nums[-k:] + nums[:-k]
        def reverse(l,r):
            while l<r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp 
                l += 1
                r -= 1
        k %= len(nums) 
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

        

        