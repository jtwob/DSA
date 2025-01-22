class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sum = 0
        for round in range(len(grid[0])):
            round_max = 0
            for row in grid:
                row_max = 0
                for val in row:
                    if val > row_max:
                        row_max = val
                row.remove(row_max)
                if round_max < row_max:
                    round_max = row_max
            sum += round_max
        return sum

