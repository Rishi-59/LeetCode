class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        l = 1
        st = set()
        for i in nums:
            st.add(i)

        for i in st:

            if i - 1 not in st:
                
                ct = 1
                x = i

                while x + 1 in st:
                    ct += 1
                    x += 1
                
                l = max(l,ct)
        
        return l