class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.player1 = set()
        self.player2 = set()
        
    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if player == 1:
            self.player1.add((row, col))
            # check row
            for c in range(self.n):
                if (row, c) not in self.player1:
                    break
            else:
                return 1

            # check col
            for r in range(self.n):
                if (r, col) not in self.player1:
                    break
            else:
                return 1

            # check diagonals
            for i in range(self.n):
                if (i, i) not in self.player1:
                    break
            else:
                return 1

            for i in range(self.n):
                if (i, self.n - 1 - i) not in self.player1:
                    break
            else:
                return 1


        else: # player2
            self.player2.add((row, col))
            # check row
            for c in range(self.n):
                if (row, c) not in self.player2:
                    break
            else:
                return 2
                
            # check col
            for r in range(self.n):
                if (r, col) not in self.player2:
                    break
            else:
                return 2

            # check diagonals
            for i in range(self.n):
                if (i, i) not in self.player2:
                    break
            else:
                return 2

            for i in range(self.n):
                if (i, self.n - 1 - i) not in self.player2:
                    break
            else:
                return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
