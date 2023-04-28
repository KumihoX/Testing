class Solution:

    @staticmethod
    def longest_increasing_path(matrix: list[list[int]]):
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        if type(matrix) is list:
            ROWS = len(matrix)
            for r in range(ROWS):
                if type(matrix[r]) is list:
                    COLS = len(matrix[0])
                    for c in range(COLS):
                        if type(matrix[r][c]) is int:
                            if matrix[r][c] > 2 ** 31 - 1 or matrix[r][c] % 1 != 0 or COLS > 200:
                                dp = {}
                                break
                            dfs(r, c, -1)
                        else: break
                else: break
        return max(dp.values())
