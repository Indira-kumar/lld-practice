from abc import ABC
from app.models.symbol import Symbol
from app.models.player_type_enum import PlayerTypeEnum


class Player(ABC):
    def __init__(self, symbol: Symbol, player_type: PlayerTypeEnum):
        self.symbol: Symbol = symbol
        self.player_type: PlayerTypeEnum = player_type
