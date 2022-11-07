class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = str(num)
        temp = list(temp)
        print(temp)
        for i in range(len(temp)):
            if temp[i] == "6":
                temp[i] = "9"
                break
        temp = "".join(temp)
        return int(temp)
                