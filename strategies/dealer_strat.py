from game.rules import get_player_value


class DealerStrat:
    @staticmethod
    def get_move(player_cards, dealer_card):
        if get_player_value(player_cards) > 17:
            return "n"
        else:
            return "y"
