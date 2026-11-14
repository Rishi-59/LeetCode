class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l,r):
            pivot = nums[r]
            lt, i, gt = l, l, r
            while i <= gt:
                if nums[i] < pivot:
                    nums[i] , nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
        
            if k < lt:
                return quick_select(l, lt-1)
            elif k > gt:
                return quick_select(gt+1, r)
            else:
                return pivot
        
        return quick_select(0,len(nums)-1)

