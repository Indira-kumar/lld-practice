from typing import Dict
from app.models.board import Board
from app.models.move import Move
from app.strategies.game_winning_strategy import GameWinningStrategy


class OrderOneGameWinningStrategy(GameWinningStrategy):
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.row_counts: Dict[int, Dict[str, int]] = {}
        self.col_counts: Dict[int, Dict[str, int]] = {}
        self.diagonal_count: Dict[str, int] = {}
        self.anti_diagonal_count: Dict[str, int] = {}

        self._initialize_counts()
    
    def _initialize_counts(self):
        for i in range(self.dimension):
            self.row_counts[i] = {}
            self.col_counts[i] = {}
    
    def check_winner(self, board: Board, last_move: Move) -> bool:
        cell = last_move.cell
        row = cell.row
        col = cell.col
        symbol = last_move.player.symbol.char
        
        if symbol not in self.row_counts[row]:
            self.row_counts[row][symbol] = 0
        self.row_counts[row][symbol] += 1
        
        if self.row_counts[row][symbol] == self.dimension:
            return True
        
        if symbol not in self.col_counts[col]:
            self.col_counts[col][symbol] = 0
        self.col_counts[col][symbol] += 1
        
        if self.col_counts[col][symbol] == self.dimension:
            return True
        
        if row == col:
            if symbol not in self.diagonal_count:
                self.diagonal_count[symbol] = 0
            self.diagonal_count[symbol] += 1
            
            if self.diagonal_count[symbol] == self.dimension:
                return True
        
        if row + col == self.dimension - 1:
            if symbol not in self.anti_diagonal_count:
                self.anti_diagonal_count[symbol] = 0
            self.anti_diagonal_count[symbol] += 1
            
            if self.anti_diagonal_count[symbol] == self.dimension:
                return True

        return False
    
    def reset(self):
        self._initialize_counts()
        self.diagonal_count.clear()
        self.anti_diagonal_count.clear()
