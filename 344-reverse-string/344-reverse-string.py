class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i = 0 
        # j = len(s)-1
        # while i < j:
        #     s[i] , s[j] = s[j] , s[i]
        #     i+=1
        #     j-=1
        
        stack = []
        for char in s:
            stack.append(char)
        i = 0
        while i < len(s):
            char = stack.pop()
            s[i] = char
            i+=1
        
        