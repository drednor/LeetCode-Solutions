class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = ""
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
                continue
            stack.append(char)
            
        return "".join(stack)