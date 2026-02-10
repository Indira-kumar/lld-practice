from typing import Optional


class User:
    def __init__(self, name, email: Optional[str] = None):
        self.name = name
        self.email = email
