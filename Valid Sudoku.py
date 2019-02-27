'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following
'''

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check_lines(board):
            for i in range(len(board)):
                horiz = set()
                vert = set()
                for j in range(len(board[0])):
                    if board[i][j] in horiz or board[j][i] in vert:
                        return False

                    if not board[i][j] == '.':
                        horiz.add(board[i][j])
                    if not board[j][i] == '.':
                        vert.add(board[j][i])
            return True

        def check_box(board):
            for x3 in range(0, len(board), 3):
                for y3 in range(0, len(board[0]), 3):
                    s = set()
                    for i in range(3):
                        for j in range(3):
                            cur = board[i + x3][j + y3]
                            if cur in s:
                                return False
                            if cur not in '.':
                                s.add(cur)
            return True

        return check_lines(board) and check_box(board)
