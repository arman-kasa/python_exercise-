"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    'J', 'Q', 'K' = 10;  'A' = 1;  '2'-'10' = numerical value.
    """
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Returns the higher card, or a tuple of both cards if equal in value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value (1 or 11) for an upcoming ace.

    An ace already in hand counts as 11, so the new ace must be 1.
    Otherwise pick 11 unless it would bust the hand (total > 21).
    """
    if 'A' in (card_one, card_two):
        return 1

    hand_value = value_of_card(card_one) + value_of_card(card_two)
    return 11 if hand_value + 11 <= 21 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack' (two cards worth 21).

    That requires exactly one ace plus one ten-valued card.
    """
    hand = (card_one, card_two)
    return 'A' in hand and any(card in ('10', 'J', 'Q', 'K') for card in hand)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand (cards of the same value)."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if the player can double down (hand totals 9, 10, or 11)."""
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
