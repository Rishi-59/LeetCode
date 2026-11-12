class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        inv = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        curr = []
        for i in s:
            if i not in inv.keys():
                curr.append(i)
            elif curr and i in inv.keys() and curr[-1] == inv[i]:
                curr.pop()
            else:
                return False
            
        return len(curr) == 0

        