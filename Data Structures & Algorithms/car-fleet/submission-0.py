class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        target_time = [(target - position[i]) / speed[i] for i in range(len(position))]

        pos_speed_time = sorted(list(zip(position, speed, target_time)), key=lambda x: x[0])
        print(pos_speed_time)
        stack = [pos_speed_time[-1]]

        for i in range(len(pos_speed_time) - 2, -1, -1):

            if pos_speed_time[i][2] > stack[-1][2]:
                stack.append(pos_speed_time[i])

            print(stack)
        return len(stack)
            
