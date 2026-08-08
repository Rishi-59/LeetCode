class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        p = ""

        while l < len(strs[0]):
            l += 1
            c = strs[0][:l]

            for i in range(len(strs)):
                if strs[i][:l] != c:
                    return p

            p = c

        return p