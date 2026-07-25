class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ###############################
        # p = []
        # n = []

        # for i in nums:
        #     if i < 0:
        #         n.append(i)
        #     else:
        #         p.append(i)

        # nums = []
        # for i in range(len(n)):
        #     nums.append(p[i])
        #     nums.append(n[i])
        
        # return nums
        
        ###############################
        n = len(nums)
        ans = [0] * n
        p = 0
        n = 1

        for i in nums:
            if i > 0:
                ans[p] = i
                p += 2
            else:
                ans[n] = i
                n += 2
        
        return ans
            
                
