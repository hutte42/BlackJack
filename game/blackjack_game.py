from deck.deck_of_cards import Deck
from game.rules import get_player_value, game_result
import time


def hand_to_string(hand):
    return " , ".join(str(card) for card in hand)


class BlackJackGame:
    def __init__(self, num_decks=1, do_delay=True, verbose=True):
        self.do_delay = do_delay
        self.verbose = verbose
        self.num_decks = num_decks
        self.num_decks_reshuffle = 26 * num_decks
        self.deck = Deck(num_decks)
        self.cards_dealer = []
        self.cards_player = []
        self.game_over = False
        self.game_outcomes = []

    def start_game(self):
        self.game_over = False
        if self.verbose:
            print("New game")
        self.cards_dealer = []
        if self.deck.get_num_cards_left() < self.num_decks_reshuffle:
            self.deck = Deck(self.num_decks)
        for _ in range(0, 2):
            self.cards_dealer.append(self.deck.draw_card())
        if self.verbose:
            print(f"Dealer cards: ??? , {self.cards_dealer[1]}")
        self.cards_player = []
        for _ in range(0, 2):
            self.cards_player.append(self.deck.draw_card())
        if self.verbose:
            print(f"Your cards: {hand_to_string(self.cards_player)}")

    def get_user_action_via_input(self):
        if self.game_over:
            print("The game is already over...")
        else:
            do_draw = input("Kérsz kártyát?(y/n) ")
            if do_draw == "y":
                self.cards_player.append(self.deck.draw_card())
                if self.verbose:
                    print(f"Your cards: {hand_to_string(self.cards_player)}")
                if get_player_value(self.cards_player) > 21:
                    if self.verbose:
                        print("BUST!")
                        print("You have lost...")
                    self.game_over = True
                    self.game_outcomes.append(-1)
                else:
                    self.get_user_action_via_input()

    def get_user_action_via_strategy(self, strategy):
        if self.game_over:
            print("The game is already over...")
        else:
            do_draw = strategy.get_move(player_cards=self.cards_player, dealer_card=self.cards_dealer[1])
            if do_draw == "y":
                self.cards_player.append(self.deck.draw_card())
                if self.verbose:
                    print(f"Your cards: {hand_to_string(self.cards_player)}")
                if get_player_value(self.cards_player) > 21:
                    if self.verbose:
                        print("BUST!")
                        print("You have lost...")
                    self.game_over = True
                    self.game_outcomes.append(-1)
                else:
                    self.get_user_action_via_strategy(strategy)

    def dealer_action(self):
        if self.game_over:
            print("The game is already over...")
        else:
            if self.verbose:
                print(f"Dealer cards: {hand_to_string(self.cards_dealer)}")
            dealer_value = get_player_value(self.cards_dealer)
            if dealer_value > 21:
                if self.verbose:
                    print("Dealer bust.\nYou win!!!!!!")
                self.game_over = True
                self.game_outcomes.append(1)
            elif dealer_value < 17:
                if self.do_delay:
                    time.sleep(3)
                self.cards_dealer.append(self.deck.draw_card())
                self.dealer_action()
            else:
                if self.verbose:
                    print("Dealer stops.")
                if self.do_delay:
                    time.sleep(3)
                winner = game_result(cards_dealer=self.cards_dealer, cards_player=self.cards_player)
                if winner == 1:
                    if self.verbose:
                        print("You win!!!!!!")
                    self.game_outcomes.append(1)
                elif winner == 0:
                    if self.verbose:
                        print("It's a draw.")
                    self.game_outcomes.append(0)
                elif winner == -1:
                    if self.verbose:
                        print("You have lost...")
                    self.game_outcomes.append(-1)
                self.game_over = True


if __name__ == '__main__':
    a = BlackJackGame()
    a.start_game()
    a.get_user_action_via_input()
    if not a.game_over:
        a.dealer_action()