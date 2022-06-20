class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        temp = int(s)
        temp += 1
        temp = str(temp)
        result = map(int, temp)
        return result