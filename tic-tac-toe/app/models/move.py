from app.models.cell import Cell
from app.models.player import Player


class Move:
    def __init__(self, cell: Cell, player: Player):
        self.cell = cell
        self.player = player
