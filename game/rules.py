def game_result(cards_dealer, cards_player):
    """

    :returns     1 if player won
                -1 if dealer won
                0 if drawn
    """
    value_dealer = get_player_value(cards_dealer)
    value_player = get_player_value(cards_player)
    if value_dealer > 21:
        return 1
    if value_player > 21:
        return -1
    if value_player > value_dealer:
        return 1
    if value_player < value_dealer:
        return -1
    if value_player == value_dealer:
        return 0


def get_card_value(card, ace_is_one):
    if card.symbol in ["J", "Q", "K"]:
        return 10
    if card.symbol == "A":
        return 1 if ace_is_one else 11
    return int(card.symbol)


def get_player_value(cards):
    value_sum = 0
    for card in cards:
        value_sum += get_card_value(card, False)
    if value_sum > 21:
        value_sum = 0
        for card in cards:
            value_sum += get_card_value(card, True)
    return value_sum

