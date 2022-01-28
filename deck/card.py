class Card:
    def __init__(self, colour, symbol):
        self.colour = colour
        self.symbol = symbol.upper()

    def __repr__(self):
        return f"{self.symbol} of {self.colour}"