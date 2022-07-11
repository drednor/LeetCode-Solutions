class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def ph(nums, sub,result):
            if len(nums) == 0:
                result.append(sub)
                return
            temp = int(nums[0])
            if temp >= 7:
                start = (temp-2)*3
                if temp == 8:
                    start += 1
                    end = start+3
                elif temp == 9:
                    start += 1
                    end = start+4
                else:
                    end = start + 4
            else:
                start = (temp-2)*3
                end = start+3
            for i in range(start, end):
                char = chr(ord("a") + i)
                ph(nums[1:],sub+char,result)
            return result
        return ph(digits, "",[])
    
        

        # def ph(s,sub, result):
        #     if len(s) == 0:
        #         result.append(sub)
        #         return
        #     char = s[0]
        #     digit = int(char)
        #     if char >= "7":
        #         start = (digit-2)*3
        #         if char == "8":
        #             start += 1
        #             end = start+3
        #         elif char == "9":
        #             start += 1
        #             end = start+4
        #         else:
        #             end = start + 4
        #     else:
        #         start = (digit-2)*3
        #         end = start+3
        #     for i in range(start,end):
        #         temp = chr(ord("a") + i)
        #         ph(s[1:],sub+temp,result)
        #     return result
        # return ph(digits,"",[])