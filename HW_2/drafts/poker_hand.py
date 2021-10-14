ex_hand = "AC TC JC KC QD"

"""
Legend:
Royal Flush  = 10
Straight Flush = 9
Four of a Kind = 8
Full House = 7
Flush = 6
Straight = 5
Three of a kind = 4
Two Pairs = 3
Pair = 2
High Card = 1
"""


def convert_values(symbols):
    converted = []
    for s in symbols:
        if s == "T":
            converted.append("10")
        elif s == "J":
            converted.append("11")
        elif s == "Q":
            converted.append("12")
        elif s == "K":
            converted.append("13")
        elif s == "A":
            converted.append("14")
        else:
            converted.append(s)

    return converted


def check_straight(values):
    for v in range(0, 5):
        values[v] = int(values[v])
    values.sort()

    i = 0
    while values[i] +1 == values[i+1]:
        i += 1
        if i == 4:
            return 5
    else:
        return 0


def check_flush(symbols):
    j = 0
    while symbols[j] == symbols[j+1]:
        j += 1
        if j == 4:
            return 6
    else:
        return 0


def check_pairs(values):
    for i in range(0, 5):
        counter = values.count(values[i])

        if counter == 4:
            return 8

        elif counter == 3:
            if i == 0:
                if values[3] == values[4]:
                    return 7
                else:
                    return 4
            elif i > 0:
                return 4

        elif counter == 2:
            if i == 0:
                for j in range(2, 5):
                    cnt = values.count(values[j])
                    if cnt == 1:
                        if values[3] == values[4]:
                            return 3
                        else:
                            return 2
                    elif cnt == 2:
                        return 3
                    elif cnt == 3:
                        return 7
            if i == 1:
                if values[3] == values[4]:
                    return 3
            if i > 1:
                return 2

        elif counter == 1:
            if i == 3:
                return 1


def poker_hand(hand):
    rank = 0
    # Retrieving data from str-hand
    hand_split = hand.split()

    hand_symbols = [s[-1] for s in hand_split]
    values = [v[0] for v in hand_split]
    values_converted = convert_values(values)

    # Checking for rank
    is_straight = check_straight(values_converted)
    is_flush = check_flush(hand_symbols)
    is_pair = check_pairs(values_converted)

    # Checking if straight flush or royal straight flush
    if is_straight and is_flush:
        if values_converted[0] == 10:
            rank = 10
        else:
            rank = 9

    # Checking what to print
    if rank < 9:
        rank = max(is_pair, is_flush, is_straight, 1)

    ranks_titles = ["Error", "High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush",
                    "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

    return ranks_titles[rank]


poker_hand("8D 8C 9S JS AC")
