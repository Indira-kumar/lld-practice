from enum import Enum

class MoveResultEnum(Enum):
    INVALID_MOVE = "INVALID_MOVE"
    VALID_MOVE = "VALID_MOVE"
    WIN = "WIN"
    DRAW = "DRAW"