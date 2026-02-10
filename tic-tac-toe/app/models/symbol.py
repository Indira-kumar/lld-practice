class Symbol:
    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError("Symbol must be a single character")
        self.char = char

    def __str__(self) -> str:
        return self.char

    def __eq__(self, other) -> bool:
        if not isinstance(other, Symbol):
            return False
        return self.char == other.char

    def __hash__(self) -> int:
        return hash(self.char)
