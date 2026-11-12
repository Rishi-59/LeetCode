class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s2) < len(s1):
            return False
        s1_f = Counter(s1)
        l,r= 0, len(s1) - 1
        c_f = {}
        for i in range(len(s1)):
            c_f[s2[i]] = c_f.get(s2[i],0) + 1
        # c_f = {c_f[s2[i]] += 1 for i in range(len(s1)) if s2[i] in c_f.keys() else s2[i] : 1}
        while r < len(s2):
            if c_f == s1_f:
                return True
            else:
                # print(r)
                # print(c_f)
                if r+1 < len(s2):
                    c_f[s2[l]] -= 1
                    if c_f[s2[l]] == 0:
                        del c_f[s2[l]]
                    l+=1
                    r+=1
                    c_f[s2[r]] = c_f.get(s2[r],0) + 1
                else:
                    return False
            


        