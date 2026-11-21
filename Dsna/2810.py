class Solution:
    def finalString(self, s: str) -> str:

        #build a deque, as you traverse you append left, you see an i, you skip, and start appending right until you see another i, 
        #reverse it based on the number of "i"s in s, even number (0 included) you reverse odd number you dont

        dq = deque()
        i_count = 0
        reverse_i = False
        for char in s:
            if char == "i":
                reverse_i = not reverse_i
                i_count += 1
                continue
            
            if reverse_i == False:
                dq.appendleft(char)
            else:
                dq.append(char)

        if i_count%2 == 0:
            return "".join(dq)[::-1]
        else:
            return "".join(dq)

        #print(dq)