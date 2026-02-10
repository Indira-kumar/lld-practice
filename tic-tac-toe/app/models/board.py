from app.models.cell import Cell


class Board:
    def __init__(self, size: int):
        self.dimension = size
        self.grids = [[Cell(i, j) for j in range(size)] for i in range(size)]

    def get_cell(self, row: int, col: int):
        return self.grids[row][col]

    def display_board(self):
        for i in range(self.dimension):
            row_display = ""
            for j in range(self.dimension):
                cell = self.grids[i][j]
                symbol_str = str(cell.symbol.char) if cell.symbol else " "
                row_display += f" {symbol_str} "
                if j < self.dimension - 1:
                    row_display += "|"
            print(row_display)

            if i < self.dimension - 1:
                print("-" * (4 * self.dimension - 1))
