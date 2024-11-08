class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        if len(s) % 2 != 0:
            return False

        stk = deque()
        for b in s:
            if b == "(":
                stk.appendleft("(")
            elif b == "[":
                stk.appendleft("[")
            elif b == "{":
                stk.appendleft("{")
            
            if len(stk) == 0:
                return False

            if len(stk) != 0:
                if b == ")" and stk[0] != "(":
                    return False
                elif b == ")" and stk[0] == "(":
                    stk.popleft()
                if b == "]" and stk[0] != "[":
                    return False
                elif b == "]" and stk[0] == "[":
                    stk.popleft()
                if b == "}" and stk[0] != "{":
                    return False
                elif b == "}" and stk[0] == "{":
                    stk.popleft()

        return len(stk) == 0 