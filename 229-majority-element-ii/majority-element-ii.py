class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr1 = 0
        ctr2 = 0
        n = len(nums)
        el1 = el2 = float('inf')
        for num in nums:
            if ctr1 == 0 and el2 != num:
                ctr1 += 1
                el1 = num
            elif ctr2 == 0 and el1 != num:
                ctr2 += 1
                el2 = num
            elif el1 == num:
                ctr1 += 1
            elif el2 == num:
                ctr2 += 1
            else:
                ctr1 -= 1
                ctr2 -= 1
        
        mm = n / 3
        ls = []
        ctr1 = ctr2 = 0
        for i in range(n):
            if nums[i] == el1:
                ctr1 += 1
            elif nums[i] == el2:
                ctr2 += 1
        if ctr1 > mm:
            ls.append(el1)
        if ctr2 > mm:
            ls.append(el2)
        
        return sorted(ls)
        # n = len(nums)
        # mm = n / 3
        # hm = {}
        # ls = []

        # for i in range(n):
        #     hm[nums[i]] = hm.get(nums[i],0) + 1
        #     if hm[nums[i]] > mm and nums[i] not in ls:
        #         ls.append(nums[i])

        # return ls