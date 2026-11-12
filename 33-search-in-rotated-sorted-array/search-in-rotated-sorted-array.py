class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target not in set(nums):
            return -1
        if len(nums) <= 1:
            if nums[0] != target:
                return -1
            return 0
        
        i,j = 0,1

        while j < len(nums)-1 and nums[i] < nums[j]:
            i+=1
            j+=1

        print(i,j)
        # if target < nums[0] and target > nums[-1]:
        #     return -1

        if j == len(nums)-1 and nums[0] <= nums[-1]:
            l,r = 0, len(nums)-1
        elif target <= nums[-1]: #right j,r  
            l,r = j,len(nums)-1
        else : #left l,i
            l,r = 0 , i

        print(l,r)
        while l <= r:
            m = (l+r) // 2
            print(m)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else: 
                l = m + 1
        
        return -1
            