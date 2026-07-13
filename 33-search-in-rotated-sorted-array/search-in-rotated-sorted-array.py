class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r = 0 , len(nums) -1

        while l <= r:
            mid = l + (r-l) // 2

            if target == nums[mid]:
                return mid

            # left is sorted
            if nums[l] <= nums[mid]:
                # does it come in sorted left region
                if nums[l] <= target and target <= nums[mid]:
                    # eliminate right
                    r = mid - 1
                # not in left sorted region
                else:
                    # eliminate left
                    l = mid + 1
            # right is sorted
            else:
                # does it come in right sorted region
                if nums[mid] <= target and target <= nums[r]:
                    # eliminate left
                    l = mid + 1
                # not in right sorted region
                else:
                    # eliminate right
                    r = mid - 1

        return -1