class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        # update current player in rows and cols array
        self.rows[row] += current_player
        self.cols[col] += current_player

        # update diagonal

        if row == col:
            self.diagonal += current_player

        # update anti-diagonal
        if col == len(self.cols) - row - 1:
            self.anti_diagonal += current_player

        # check if the current player wins
        if abs(self.rows[row]) == self.n or \
                abs(self.cols[col]) == self.n or \
                abs(self.diagonal) == self.n or \
                abs(self.anti_diagonal) == self.n:
            return player

        # no one wins
        return 0

if __name__ == '__main__':
    ticTacToe = TicTacToe(3)
    moves = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
    for move in moves:
        print(f'Result: {ticTacToe.move(move[0], move[1], player=move[2])} for player {move[2]}')