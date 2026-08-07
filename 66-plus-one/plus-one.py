class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits
        # carry = 0
        # for i in range(len(digits)-1,-1,-1):
        #     total = digits[i] + 1
        #     digits[i] = total % 10
        #     carry = total // 10
        #     if carry == 0:
        #         break
        # if carry:
        #     digits = [1] + digits
        # return digits