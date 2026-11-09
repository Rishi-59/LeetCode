class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr_l = len(nums)
        ans = []
        for i in range(arr_l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            l , r = i+1 , arr_l-1

            while l < r:

                total = nums[l] + nums[r]

                if total == target :
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total < target:
                    l+=1
                else:
                    r-=1

        
        return ans
            
                
