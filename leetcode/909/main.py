from typing import List


class Solution:
    cache = {}

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        self.cache = {}
        self.dfs(0, 0, board, n)
        return self.cache[n * n - 1] if (n * n - 1) in self.cache else -1

    def dfs(self, moves: int, curr_pos: int, board: List[List[int]], n: int):
        if curr_pos == n * n - 1:
            return

        new_positions = []
        for steps in range(1, 7):
            new_position = min(curr_pos + steps, n * n - 1)
            r, c = self.get_board_coordinates(new_position, board)

            if board[r][c] != -1:
                new_position = board[r][c]-1

            if new_position in self.cache and self.cache[new_position] <= moves + 1:
                continue
            else:
                new_positions.append(new_position)
                self.cache[new_position] = moves + 1
        for pos in new_positions:
            self.dfs(moves + 1, pos, board, n)

    def get_board_coordinates(self, destination: int, board) -> (int, int):
        n = len(board)
        r = destination // n

        if r % 2:
            c = (n - 1) - (destination % n)
        else:
            c = destination % n
        r = (n-1) - r
        return (r, c)


if __name__ == '__main__':
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    sol = Solution()
    print(sol.snakesAndLadders(board))
