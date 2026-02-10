from typing import List, Optional
from app.models.game import Game
from app.models.player import Player
from app.models.move import Move
from app.models.board import Board
from app.models.move_result_enum import MoveResultEnum
from app.models.game_status_enum import GameStatusEnum
from app.strategies.game_winning_strategy import GameWinningStrategy


class GameController:
    def create_game(self, dimension: int, players: List[Player], 
                    strategies: List[GameWinningStrategy]) -> Game:
        try:
            game = Game.create() \
                .with_board(Board(dimension)) \
                .add_players(players) \
                .add_winning_strategies(strategies) \
                .build()
            
            print(f"Game created successfully! {len(players)} players, {dimension}x{dimension} board")
            return game
            
        except ValueError as e:
            print(f"Error creating game: {e}")
            raise
    
    def make_move(self, game: Game, row: int, col: int) -> MoveResultEnum:
        if game.game_status != GameStatusEnum.IN_PROGRESS:
            print("Game is already over!")
            return MoveResultEnum.INVALID_MOVE

        if row < 0 or row >= game.board.dimension or col < 0 or col >= game.board.dimension:
            print(f"Invalid coordinates: ({row}, {col})")
            return MoveResultEnum.INVALID_MOVE

        cell = game.board.get_cell(row, col)

        if not cell.is_empty():
            print(f"Cell ({row}, {col}) is already occupied!")
            return MoveResultEnum.INVALID_MOVE

        current_player = game.players[game.current_player_index]

        move = Move(cell, current_player)
        is_winning_move = game.make_move(move)

        if is_winning_move:
            game.game_status = GameStatusEnum.COMPLETED
            game.winner = current_player
            print(f"🎉 Player {current_player.symbol.char} wins!")
            return MoveResultEnum.WIN

        if len(game.moves) == game.board.dimension ** 2:
            game.game_status = GameStatusEnum.DRAW
            print("Game ended in a draw!")
            return MoveResultEnum.DRAW
        
        return MoveResultEnum.VALID_MOVE
    
    def undo(self, game: Game) -> bool:
        if game.game_status == GameStatusEnum.COMPLETED:
            game.game_status = GameStatusEnum.IN_PROGRESS
            game.winner = None
        
        success = game.undo()
        if success:
            print("Move undone successfully!")
        return success
    
    def display_board(self, game: Game) -> None:
        game.board.display_board()
    
    def get_winner(self, game: Game) -> Optional[Player]:
        return game.winner
    
    def get_game_status(self, game: Game) -> GameStatusEnum:
        return game.game_status
    
    class Builder:
        def __int__(self):
            self._game = None