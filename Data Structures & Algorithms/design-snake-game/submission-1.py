class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.w = width
        self.h = height
        self.pos = [0, 0]
        self.food = food
        self.i = 0
        self.score = 0
        self.body = []

    def move(self, direction: str) -> int:

        # calculate next pos
        nr, nc = self.pos
        if direction == "U": nr -= 1
        if direction == "D": nr += 1
        if direction == "L": nc -= 1
        if direction == "R": nc += 1

        # check if hit wall
        if not 0 <= nr < self.h or not 0 <= nc < self.w: return -1

        # check if eat food
        if self.i < len(self.food) and nr == self.food[self.i][0] and nc == self.food[self.i][1]:
            self.score += 1
            self.i += 1
            self.body.append([nr, nc])
        else: # if empty block
            for pr, pc in self.body[1:]:
                if nr == pr and nc == pc: # check if eat itself
                    return -1
            # update current body blocks
            for i in range(len(self.body) - 1):
                self.body[i] = self.body[i + 1]
            if self.body:
                self.body[-1] = [nr, nc]

        self.pos = [nr, nc]

        return self.score




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
