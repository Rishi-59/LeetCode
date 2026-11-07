class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i, v in enumerate(nums):
            if target - v in visited.keys():
                return [visited[target - v], i]
            visited[v] = i
            # print(visited)
        