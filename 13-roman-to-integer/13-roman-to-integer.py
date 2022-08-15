class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        
        translation ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for char in s:
            res += translation[char]
        return res