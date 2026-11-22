class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        #sort by distance from close to far
        #find out how much time it takes
        #if the farther group takes less time itll form a group
        #for each car check to see if it can catch up, if yes add to the stack

        cars = sorted(list(zip(position,speed)), reverse=True)

        # time = [0] * len(position)
        # for i in range(len(position)):
        #     time[i] = (target-cars[i][0])/cars[i][1]

        time = [(target-cars[i][0])/cars[i][1] for i in range(len(position))]

        fleet = [time[0]]
        for i in range(1,len(time)):
            if time[i] > fleet[-1]:
                fleet.append(time[i])

        return len(fleet)
        