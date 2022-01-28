from deck.card import Card
from game.rules import game_result


# Goals for next time játék mehanizmus; github
if __name__ == '__main__':
    result = game_result(cards_dealer=[Card("red", "J"), Card("black", "1")],
                         cards_player=[Card("red", "2"), Card("black", "k")])
    print(result)
    # list comprehension practice
    a = [1, 2, 3]
    # without list comprehension
    b = []
    for elem in a:
        b.append(elem * 2)
    # with list comprehension
    c = [elem * 2 for elem in a]
    print("C")

