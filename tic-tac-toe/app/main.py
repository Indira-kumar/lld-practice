from app.models.bot import Bot
from app.models.human_player import HumanPlayer
from app.models.symbol import Symbol
from app.models.user import User
from app.models.player_type_enum import PlayerTypeEnum
from app.strategies.random_bot_playing_strategy import RandomBotPlayingStrategy
from app.strategies.order_one_game_winning_strategy import OrderOneGameWinningStrategy
from app.controller.game_controller import GameController


def main():
    print("Welcome to Tic-Tac-Toe!\n")
    
    me = User("Indira Kumar", "indira.kumar@example.com")
    player1 = HumanPlayer(me, Symbol('X'))
    player2 = Bot(Symbol('O'), RandomBotPlayingStrategy())
    
    controller = GameController()
    game = controller.create_game(3, [player1, player2], [OrderOneGameWinningStrategy(3)])
    
    print("\nInitial Board:")
    controller.display_board(game)
    print()
    
    print("Move 1: Human plays at (0, 0)")
    controller.make_move(game, 0, 0)
    controller.display_board(game)
    print()
    
    current_player = game.players[game.current_player_index]
    if current_player.player_type == PlayerTypeEnum.BOT:
        print("Move 2: Bot's turn...")
        bot_cell = current_player.make_move(game.board)
        if bot_cell:
            print(f"Bot plays at ({bot_cell.row}, {bot_cell.col})")
            controller.make_move(game, bot_cell.row, bot_cell.col)
            controller.display_board(game)
            print()
    
    print("Move 3: Human plays at (1, 1)")
    controller.make_move(game, 1, 1)
    controller.display_board(game)
    print()
    
    current_player = game.players[game.current_player_index]
    if current_player.player_type == PlayerTypeEnum.BOT:
        print("Move 4: Bot's turn...")
        bot_cell = current_player.make_move(game.board)
        if bot_cell:
            print(f"Bot plays at ({bot_cell.row}, {bot_cell.col})")
            controller.make_move(game, bot_cell.row, bot_cell.col)
            controller.display_board(game)
            print()
    
    # print("Testing UNDO feature...")
    # controller.undo(game)
    # controller.display_board(game)
    # print()
    
    # current_player = game.players[game.current_player_index]
    # if current_player.player_type == PlayerTypeEnum.BOT:
    #     print("Move 4 again: Bot's turn...")
    #     bot_cell = current_player.make_move(game.board)
    #     if bot_cell:
    #         print(f"Bot plays at ({bot_cell.row}, {bot_cell.col})")
    #         controller.make_move(game, bot_cell.row, bot_cell.col)
    #         controller.display_board(game)
    #         print()

    print("Move 5: Human plays at (2, 2)")
    controller.make_move(game, 2, 2)
    controller.display_board(game)
    print()
    
    if game.winner:
        print(f"\n🎉 Game Over! Winner: Player {game.winner.symbol.char}")
    else:
        print(f"\nGame Status: {game.game_status.value}")
    
    print("\nGame Demo Complete!")


if __name__ == "__main__":
    main()
