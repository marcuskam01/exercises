class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = deque()
        for b in s:
            #push open brackets to stack top
            if b == '(' or b == '{' or b == '[':
                bracket_stack.append(b)

            #pop from top if not matching return false
            elif b == ')' and bracket_stack and bracket_stack[-1] == '(':
                bracket_stack.pop()
            elif b == '}' and bracket_stack and bracket_stack[-1] == '{':
                bracket_stack.pop()
            elif b == ']' and bracket_stack and bracket_stack[-1] == '[':
                bracket_stack.pop()
            
            else:
                return False
        #check if anything remains
        return len(bracket_stack) == 0