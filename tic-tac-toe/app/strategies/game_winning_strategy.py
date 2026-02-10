from abc import ABC, abstractmethod
from app.models.board import Board
from app.models.move import Move

class GameWinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, move: Move) -> bool:
        pass