class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter, defaultdict
        freq_table= defaultdict(list)
        freq_list = []
        for word in strs:
            freq = tuple(sorted(Counter(word).items()))
            if freq not in freq_list:
                freq_list.append(freq)
            i = freq_list.index(freq)
            freq_table[i].append(word)
        
        ans = []
        for key, val in freq_table.items():
            ans.append(val)

        return ans
            
            