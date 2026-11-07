class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import Counter, defaultdict
        freq_table= defaultdict(list)
        for word in strs:
            freq = tuple(sorted(Counter(word).items()))
            freq_table[freq].append(word)

        return [val for val in freq_table.values()]
            
            