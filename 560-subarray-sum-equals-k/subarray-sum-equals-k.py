class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {}
        hm[0] = 1
        count = 0
        ps = 0

        for i in range(len(nums)):
            ps += nums[i]
            target = ps - k
            count += hm.get(target,0)
            hm[ps] = hm.get(ps,0) + 1

        return count
        ################################

        # count = 0
        # n = len(nums)

        # for i in range(n):
        #     total = 0
        #     for j in range(i,n):
        #         total += nums[j] 
        #         if total == k:
        #             count += 1
        # return count
