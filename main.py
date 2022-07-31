from deck.card import Card
from game.rules import game_result
from game.blackjack_game import BlackJackGame
from strategies.always_stop import AlwaysStopStrategy
from strategies.dealer_strat import DealerStrat


# Goals for next time money system, more players, split, double
if __name__ == '__main__':
    game = BlackJackGame(do_delay=False, verbose=False, num_decks=2)
    for _ in range(10000):
        game.start_game()
        game.get_user_action_via_strategy(AlwaysStopStrategy)
        if not game.game_over:
            game.dealer_action()
    print(f"Number of draws:{game.game_outcomes.count(0)}\nNumber of wins:{game.game_outcomes.count(1)}\nNumber of losses:{game.game_outcomes.count(-1)}\n")

    game = BlackJackGame(do_delay=False, verbose=False, num_decks=2)
    for _ in range(10000):
        game.start_game()
        game.get_user_action_via_strategy(DealerStrat)
        if not game.game_over:
            game.dealer_action()
    print(f"Number of draws:{game.game_outcomes.count(0)}\nNumber of wins:{game.game_outcomes.count(1)}\nNumber of losses:{game.game_outcomes.count(-1)}\n")
