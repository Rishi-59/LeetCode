class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = []
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in visited:
                return [visited.index(tar),i]
            else:
                visited.append(nums[i])
        

            