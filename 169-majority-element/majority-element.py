class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[(len(nums)-1)//2]
        el = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                el = num
            if num == el:
                count += 1
            else:
                count -= 1
        return el             
