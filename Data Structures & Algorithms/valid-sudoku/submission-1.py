class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            horizontal = []
            vertical = []
            for a in board[i]:
                if a.isdigit():
                    horizontal.append(int(a))

            for j in range(len(board)):
                if board[j][i].isdigit():
                    vertical.append(int(board[j][i]))

            if len(horizontal) != len(set(horizontal)) or len(vertical) != len(set(vertical)):
                return False

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                box = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col].isdigit():
                            box.append(int(board[row][col]))

                if len(box) != len(set(box)):
                    return False

        return True
        