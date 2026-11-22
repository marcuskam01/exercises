class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #traverse and add num to stack

        #encounter an operator
        #pop last 2 and evaluate

        #add back to stack repeat
        #no need for deque as right pop and right append are both O(1) for list with less overhead

        sol = []

        for i, v in enumerate(tokens):
            if i > 1 and v == "+":
                num1 = sol.pop()
                num2 = sol.pop()
                sol.append(num1+num2)
            elif i > 1 and v == "-":
                num1 = sol.pop()
                num2 = sol.pop()
                sol.append(num2-num1)
            elif i > 1 and v == "*":
                num1 = sol.pop()
                num2 = sol.pop()
                sol.append(num1*num2)
            elif i > 1 and v == "/":
                num1 = sol.pop()
                num2 = sol.pop()
                sol.append(int(num2/num1))
            else:
                sol.append(int(v))

        return sol[0]