class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) -1
        while carry:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.insert(0,1)
                carry = 0
            i -= 1
        return digits
            
        
        
        #simple solution
        # s = ""
        # for i in digits:
        #     s += str(i)
        # temp = int(s)
        # temp += 1
        # temp = str(temp)
        # result = map(int, temp)
        # return result