class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in temp:
                if stack and stack[-1] == temp[i]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)
        return len(stack) == 0
                
            
        