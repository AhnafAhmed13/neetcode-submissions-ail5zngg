class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = len(board)
        M = len(board[0])
        
        # check by row
        for row in board:
            s = set()
            for num in row:
                if num != ".":
                    if num in s:
                        return False
                    s.add(num)
        print("Row valid")

        # check by col
        for c in range(M):
            s = set()
            for r in range(N):
                num = board[r][c]
                if num != ".":
                    if num in s:
                        return False
                    s.add(num)
        print("Col valid")

        # check in sub-box
        boxes = [set() for _ in range(9)]

        for r in range(N):
            for c in range(M):
                num = board[r][c]
                if num != ".":
                    box_idx = (r // 3) * 3 + (c // 3)
                    if num in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(num)

        print("Sub-box valid")
        return True

    """ for r in range(N):
            for c in range(M):
                num = board[r][c]
                # print(r, c, num, boxes)
                if num != ".":
                    match(r, c):
                        case (0 | 1 | 2, 0 | 1 | 2):
                            if num in boxes[0]:
                                return False
                            boxes[0].add(num)

                        case (0 | 1 | 2, 3 | 4 | 5):
                            if num in boxes[1]:
                                return False
                            boxes[1].add(num)

                        case (0 | 1 | 2, 6 | 7 | 8):
                            if num in boxes[2]:
                                return False
                            boxes[2].add(num)

                        case (3 | 4 | 5, 0 | 1 | 2):
                            if num in boxes[3]:
                                return False
                            boxes[3].add(num)

                        case (3 | 4 | 5, 3 | 4 | 5):
                            if num in boxes[4]:
                                return False
                            boxes[4].add(num)

                        case (3 | 4 | 5, 6 | 7 | 8):
                            if num in boxes[5]:
                                return False
                            boxes[5].add(num)

                        case (6 | 7 | 8, 0 | 1 | 2):
                            if num in boxes[6]:
                                return False
                            boxes[6].add(num)

                        case (6 | 7 | 8, 3 | 4 | 5):
                            if num in boxes[7]:
                                return False
                            boxes[7].add(num)

                        case (6 | 7 | 8, 6 | 7 | 8):
                            if num in boxes[8]:
                                return False
                            boxes[8].add(num)"""





