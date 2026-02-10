from app.models.player import Player
from app.models.symbol import Symbol
from app.models.player_type_enum import PlayerTypeEnum
from app.models.user import User


class HumanPlayer(Player):
    def __init__(self, user: User, symbol: Symbol):
        super().__init__(symbol, PlayerTypeEnum.HUMAN)
        self.user = user
