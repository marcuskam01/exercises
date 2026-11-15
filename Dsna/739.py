class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp_stack = deque()
        res = [0] * len(temperatures)
        #check newest temp to stack and compare to temp before
        #if higher then pop the last element
        #keep popping until the last existing element is higher than current
        #day to higher is then the current index - the index of the last thing that got popped
        #when there is no more higher temperature add current index and temp
        for i, t in enumerate(temperatures):
            while len(temp_stack) != 0 and t > temp_stack[-1][1]:
                ind, temp = temp_stack.pop()
                res[ind] = i - ind 
            temp_stack.append((i, t))
        
        return res
        #print(temp_stack)