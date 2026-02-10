from abc import ABC, abstractmethod
from app.models.board import Board
from app.models.cell import Cell

class BotPlayingStrategy(ABC):
    @abstractmethod
    def make_move(self, board: Board) -> Cell:
        pass