from deck.card import Card
from game.rules import game_result


# Goals for next time money system, more decks, reshufle, more players
if __name__ == '__main__':
    result = game_result(cards_dealer=[Card("red", "J"), Card("black", "1")],
                         cards_player=[Card("red", "2"), Card("black", "k")])
    print(result)
