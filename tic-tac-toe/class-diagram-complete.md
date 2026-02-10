# Tic-Tac-Toe Class Diagram

## Complete System Design

```mermaid
classDiagram
    %% Enums
    class GameStatusEnum {
        <<enumeration>>
        IN_PROGRESS
        DRAW
        COMPLETED
    }
    
    class PlayerTypeEnum {
        <<enumeration>>
        HUMAN
        BOT
    }
    
    class MoveResultEnum {
        <<enumeration>>
        INVALID_MOVE
        VALID_MOVE
        WIN
        DRAW
    }
    
    %% Core Models
    class Symbol {
        -char: str
        +__init__(char: str)
        +__str__() str
        +__eq__(other) bool
        +__hash__() int
    }
    
    class User {
        -name: str
        -email: Optional[str]
        +__init__(name: str, email: Optional[str])
    }
    
    class Cell {
        -row: int
        -col: int
        -symbol: Optional[Symbol]
        +__init__(row: int, col: int, symbol: Optional[Symbol])
        +is_empty() bool
        +set_symbol(symbol: Symbol)
        +clear_cell()
    }
    
    class Board {
        -dimension: int
        -grids: List[List[Cell]]
        +__init__(size: int)
        +get_cell(row: int, col: int) Cell
        +display_board()
        +get_empty_cells() List[Cell]
    }
    
    class Move {
        -cell: Cell
        -player: Player
        +__init__(cell: Cell, player: Player)
    }
    
    %% Player Hierarchy
    class Player {
        <<abstract>>
        -symbol: Symbol
        -player_type: PlayerTypeEnum
        +__init__(symbol: Symbol, player_type: PlayerTypeEnum)
    }
    
    class HumanPlayer {
        -user: User
        +__init__(user: User, symbol: Symbol)
    }
    
    class Bot {
        -bot_playing_strategy: BotPlayingStrategy
        +__init__(symbol: Symbol, bot_playing_strategy: BotPlayingStrategy)
        +make_move(board: Board) Cell
    }
    
    %% Strategy Pattern - Bot Playing
    class BotPlayingStrategy {
        <<abstract>>
        +make_move(board: Board)* Cell
    }
    
    class RandomBotPlayingStrategy {
        +make_move(board: Board) Cell
    }
    
    %% Strategy Pattern - Winning Detection
    class GameWinningStrategy {
        <<abstract>>
        +check_winner(board: Board, last_move: Move)* bool
    }
    
    class OrderOneGameWinningStrategy {
        -dimension: int
        -row_counts: Dict[int, Dict[str, int]]
        -col_counts: Dict[int, Dict[str, int]]
        -diagonal_count: Dict[str, int]
        -anti_diagonal_count: Dict[str, int]
        +__init__(dimension: int)
        +check_winner(board: Board, last_move: Move) bool
        -_initialize_counts()
        +reset()
    }
    
    %% Game Class with Builder
    class Game {
        -players: List[Player]
        -board: Board
        -moves: List[Move]
        -game_winning_strategies: List[GameWinningStrategy]
        -current_player_index: int
        -game_status: GameStatusEnum
        -winner: Optional[Player]
        +__init__(board: Board, players: List[Player], game_winning_strategies: List[GameWinningStrategy])
        +create()$ Builder
        +make_move(move: Move) bool
        +check_winner(move: Move) bool
        +undo() bool
    }
    
    class GameBuilder {
        <<nested in Game>>
        -_board: Optional[Board]
        -_players: List[Player]
        -_game_winning_strategies: List[GameWinningStrategy]
        +__init__()
        +with_board(board: Board) Builder
        +add_player(player: Player) Builder
        +add_players(players: List[Player]) Builder
        +add_winning_strategy(strategy: GameWinningStrategy) Builder
        +add_winning_strategies(strategies: List[GameWinningStrategy]) Builder
        -_validate()
        +build() Game
    }
    
    %% Controller
    class GameController {
        +create_game(dimension: int, players: List[Player], strategies: List[GameWinningStrategy]) Game
        +make_move(game: Game, row: int, col: int) MoveResultEnum
        +undo(game: Game) bool
        +display_board(game: Game)
        +get_winner(game: Game) Optional[Player]
        +get_game_status(game: Game) GameStatusEnum
    }
    
    %% Relationships
    
    %% Composition
    Board o-- Cell : contains
    Game *-- Board : has
    Game *-- Move : tracks
    Move *-- Cell : references
    Move *-- Player : made by
    
    %% Association
    Player -- Symbol : uses
    Cell -- Symbol : contains
    HumanPlayer -- User : has
    Bot -- BotPlayingStrategy : uses
    Game -- GameWinningStrategy : uses
    Game -- GameStatusEnum : has status
    Player -- PlayerTypeEnum : has type
    
    %% Inheritance
    Player <|-- HumanPlayer
    Player <|-- Bot
    BotPlayingStrategy <|-- RandomBotPlayingStrategy
    GameWinningStrategy <|-- OrderOneGameWinningStrategy
    
    %% Builder Pattern
    Game ..> GameBuilder
    GameBuilder ..> Game
    
    %% Controller relationships
    GameController ..> Game : manages
    GameController ..> Player : uses
    GameController ..> GameWinningStrategy : configures
    GameController ..> MoveResultEnum : returns
```

## Design Patterns

### 1. Builder Pattern
- **Class**: `Game.Builder`
- **Purpose**: Construct complex Game objects with validation
- **Benefits**: Readable construction, centralized validation, flexible configuration

### 2. Strategy Pattern
- **Interfaces**: `BotPlayingStrategy`, `GameWinningStrategy`
- **Purpose**: Encapsulate algorithms (bot moves, win detection)
- **Benefits**: Easy to add new strategies, interchangeable at runtime

### 3. Factory Pattern (Concept)
- **Usage**: Controller creates Game objects
- **Purpose**: Centralize object creation logic

### 4. Template Method (Abstract Classes)
- **Class**: `Player`
- **Purpose**: Define common structure for all player types

## Key Relationships

### Inheritance (IS-A)
- `HumanPlayer` IS-A `Player`
- `Bot` IS-A `Player`
- `RandomBotPlayingStrategy` IS-A `BotPlayingStrategy`
- `OrderOneGameWinningStrategy` IS-A `GameWinningStrategy`

### Composition (HAS-A)
- `Game` HAS-A `Board` (strong ownership)
- `Board` HAS `Cells` (strong ownership)
- `Game` HAS `Moves` (strong ownership)

### Association (USES-A)
- `Player` USES `Symbol`
- `Bot` USES `BotPlayingStrategy`
- `Game` USES `GameWinningStrategy`
- `HumanPlayer` USES `User`

### Dependency
- `GameController` depends on `Game`, `Player`, etc.
- `Move` depends on `Cell` and `Player`

## SOLID Principles Applied

### Single Responsibility
- Each class has one clear purpose
- `Cell`: Manages cell state
- `Board`: Manages grid
- `Game`: Manages game state
- `GameController`: Orchestrates operations

### Open/Closed
- Easy to add new `BotPlayingStrategy` implementations
- Easy to add new `GameWinningStrategy` implementations
- No need to modify existing code

### Liskov Substitution
- `HumanPlayer` and `Bot` are interchangeable as `Player`
- All strategies are interchangeable within their interface

### Interface Segregation
- Separate interfaces for bot playing and win detection
- No fat interfaces forcing unnecessary implementations

### Dependency Inversion
- Depend on abstractions (`BotPlayingStrategy`, `GameWinningStrategy`)
- High-level modules don't depend on low-level details

## Validation Rules (in Builder)

1. Board must exist
2. Minimum 2 players required
3. Number of players = board dimension - 1
4. Maximum 1 bot allowed
5. No duplicate symbols
6. At least one winning strategy required

## Time Complexity

- **Make Move**: O(1)
- **Check Winner**: O(1) with OrderOneGameWinningStrategy
- **Undo**: O(1)
- **Display Board**: O(n²)