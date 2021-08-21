class QuoteModel:
    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __str__(self) -> str:
        return f'<{self.body} - {self.author}'

    def __repr__(self) -> str:
        return self.__str__()
