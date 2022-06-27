class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        operators = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        stack = []
        for c in tokens:
            if c in operators:
                a , b = int(stack.pop()), int(stack.pop())
                stack.append(int(operators[c](b,a)))
            else:
                stack.append(c)
        return stack[0]
                