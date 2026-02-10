from app.models.symbol import Symbol
from app.models.player_type_enum import PlayerTypeEnum
from app.models.player import Player
from app.strategies.bot_playing_strategy import BotPlayingStrategy
from app.models.board import Board
from app.models.cell import Cell


class Bot(Player):
    def __init__(self, symbol: Symbol, bot_playing_strategy: BotPlayingStrategy):
        super().__init__(symbol, PlayerTypeEnum.BOT)
        self.bot_playing_strategy = bot_playing_strategy
    
    def make_move(self, board: Board) -> Cell:
        return self.bot_playing_strategy.make_move(board)