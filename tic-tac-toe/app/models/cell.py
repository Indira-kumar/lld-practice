from app.models.symbol import Symbol
from typing import Optional


class Cell:
    def __init__(self, row: int, col: int, symbol: Optional[Symbol] = None):
        self.row = row
        self.col = col
        self.symbol = symbol

    def is_empty(self) -> bool:
        return self.symbol is None

    def set_symbol(self, symbol: Symbol):
        if not self.is_empty():
            raise ValueError("Cell is already occupied")
        self.symbol = symbol

    def clear_cell(self):
        self.symbol = None

    def __str__(self) -> str:
        return str(self.symbol) if self.symbol else " "
