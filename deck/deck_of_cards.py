import random
from itertools import product
from deck.card import Card


# colour: hearts, diamonds, spades, clubs; symbol: 1-10, J, Q, K, A
class Deck:
    def __init__(self):
 #       self.card = [Card(colour, number) for colour, number in
 #                    product(["hearts", "diamonds", "spades", "clubs"],
 #                            [str(num) for num in range(1, 11)] + ["J", "Q", "K", "A"])]
        self.card = []
        for symbol in range(0, 4):
            if symbol == 0:
                actcolour = "hearts"
            elif symbol == 1:
                actcolour = "diamonds"
            elif symbol == 2:
                actcolour = "clubs"
            else:
                actcolour = "spades"
            for number in range(1, 15):
                if number < 11:
                    self.card.append(Card(actcolour, str(number)))
                else:
                    if number == 11:
                        self.card.append(Card(actcolour, "J"))
                    elif number == 12:
                        self.card.append(Card(actcolour, "Q"))
                    elif number == 13:
                        self.card.append(Card(actcolour, "K"))
                    else:
                        self.card.append(Card(actcolour, "A"))

    def draw_card(self):
        card_index = random.randrange(0, len(self.card))
        return self.card.pop(card_index)


if __name__ == "__main__":
    d = Deck()
    for i in range(0, 56):
        print(d.draw_card())
        print(f"{len(d.card)} cards left in the deck")
    if len(d.card) != 0:
        print(f"NOT GOOD DECK STILL HAS {len(d.card)} cards left after drawing 56 cards!!")
    a = 6