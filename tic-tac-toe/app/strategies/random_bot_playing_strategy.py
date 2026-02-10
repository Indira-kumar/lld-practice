from app.models.board import Board
from app.models.cell import Cell
from app.strategies.bot_playing_strategy import BotPlayingStrategy
import random

class RandomBotPlayingStrategy(BotPlayingStrategy):
    def make_move(self, board: Board) -> Cell:
        empty_cells = board.get_empty_cells()
        if not empty_cells:
            return None
        return random.choice(empty_cells)