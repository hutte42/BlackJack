from deck.deck_of_cards import Deck
from game.rules import get_player_value, game_result
import time


def hand_to_string(hand):
    return " , ".join(str(card) for card in hand)


class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.cards_dealer = []
        self.cards_player = []
        self.game_over = False

    def start_game(self):
        self.game_over = False
        print("New game")
        self.cards_dealer = []
        for _ in range(0, 2):
            self.cards_dealer.append(self.deck.draw_card())
        print(f"Dealer cards: ??? , {self.cards_dealer[1]}")
        self.cards_player = []
        for _ in range(0, 2):
            self.cards_player.append(self.deck.draw_card())
        print(f"Your cards: {hand_to_string(self.cards_player)}")

    def get_user_action(self):
        if self.game_over:
            print("The game is already over...")
        else:
            do_draw = input("Kérsz kártyát?(y/n) ")
            if do_draw == "y":
                self.cards_player.append(self.deck.draw_card())
                print(f"Your cards: {hand_to_string(self.cards_player)}")
                if get_player_value(self.cards_player) > 21:
                    print("BUST!")
                    print("You have lost...")
                    self.game_over = True
                else:
                    self.get_user_action()

    def dealer_action(self):
        if self.game_over:
            print("The game is already over...")
        else:
            print(f"Dealer cards: {hand_to_string(self.cards_dealer)}")
            dealer_value = get_player_value(self.cards_dealer)
            if dealer_value > 21:
                print("Dealer bust.\nYou win!!!!!!")
                self.game_over = True
            elif dealer_value < 17:
                time.sleep(3)
                self.cards_dealer.append(self.deck.draw_card())
                self.dealer_action()
            else:
                time.sleep(3)
                winner = game_result(cards_dealer=self.cards_dealer, cards_player=self.cards_player)
                if winner == 1:
                    print("You win!!!!!!")
                elif winner == 0:
                    print("It's a draw.")
                elif winner == -1:
                    print("You have lost...")
                self.game_over = True


a = BlackJackGame()
a.start_game()
a.get_user_action()
if not a.game_over:
    a.dealer_action()