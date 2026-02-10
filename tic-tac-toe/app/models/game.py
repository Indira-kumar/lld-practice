from typing import List, Optional
from app.models.board import Board
from app.models.move import Move
from app.models.player import Player
from app.models.game_status_enum import GameStatusEnum
from app.models.player_type_enum import PlayerTypeEnum
from app.strategies.game_winning_strategy import GameWinningStrategy


class Game:
    def __init__(self, board: Board, players: List[Player], 
                 game_winning_strategies: List[GameWinningStrategy]):
        self.board = board
        self.players = players
        self.game_winning_strategies = game_winning_strategies
        self.moves: List[Move] = []
        self.current_player_index: int = 0
        self.game_status: GameStatusEnum = GameStatusEnum.IN_PROGRESS
        self.winner: Optional[Player] = None

    @staticmethod
    def create():
        return Game.Builder()

    def make_move(self, move: Move) -> bool:
        current_player = self.players[self.current_player_index]
        current_player_symbol = current_player.symbol
        move.cell.set_symbol(current_player_symbol)
        self.moves.append(move)

        if self.check_winner(move):
            print(f"Player {current_player.symbol.char} wins!")
            return True
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False
    
    def check_winner(self, move: Move) -> bool:
        for strategy in self.game_winning_strategies:
            if strategy.check_winner(self.board, move):
                return True
        return False

    def undo(self):
        if not self.moves:
            print("No moves to undo.")
            return False
        last_move = self.moves.pop()
        last_move.cell.clear_cell()
        
        for strategy in self.game_winning_strategies:
            if hasattr(strategy, 'undo_move'):
                strategy.undo_move(last_move)
        
        self.current_player_index = (self.current_player_index - 1) % len(self.players)
        return True

    class Builder:
        
        def __init__(self):
            self._board: Optional[Board] = None
            self._players: List[Player] = []
            self._game_winning_strategies: List[GameWinningStrategy] = []
        
        def with_board(self, board: Board):
            self._board = board
            return self
        
        def add_player(self, player: Player):
            self._players.append(player)
            return self
        
        def add_players(self, players: List[Player]):
            self._players.extend(players)
            return self
        
        def add_winning_strategy(self, strategy: GameWinningStrategy):
            self._game_winning_strategies.append(strategy)
            return self
        
        def add_winning_strategies(self, strategies: List[GameWinningStrategy]):
            self._game_winning_strategies.extend(strategies)
            return self
        
        def _validate(self):
            if self._board is None:
                raise ValueError("Board must be set")
            
            if len(self._players) < 2:
                raise ValueError("Game must have at least 2 players")
            
            if len(self._players) != self._board.dimension - 1:
                raise ValueError(
                    f"For {self._board.dimension}x{self._board.dimension} board, "
                    f"must have exactly {self._board.dimension - 1} players"
                )
            
            bot_count = sum(1 for p in self._players if p.player_type == PlayerTypeEnum.BOT)
            if bot_count > 1:
                raise ValueError("Only one bot is allowed per game")
            
            symbols = [p.symbol.char for p in self._players]
            if len(symbols) != len(set(symbols)):
                raise ValueError("Players cannot have duplicate symbols")
            
            if len(self._game_winning_strategies) == 0:
                raise ValueError("At least one winning strategy must be provided")
        
        def build(self) -> 'Game':
            self._validate()
            return Game(self._board, self._players, self._game_winning_strategies)
