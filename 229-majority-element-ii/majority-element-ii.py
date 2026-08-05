class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mm = n / 3
        hm = {}
        ls = []

        for i in range(n):
            hm[nums[i]] = hm.get(nums[i],0) + 1
            if hm[nums[i]] > mm and nums[i] not in ls:
                ls.append(nums[i])

        return ls