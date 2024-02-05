# https://adventofcode.com/2023/day/7

import os

FILENAME = "data.txt"
# FILENAME = "data_test.txt"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")

data_trans = []
for row in data:
    print(row)
    row = row.split()
    row = [row[0], int(row[1])]
    data_trans.append(row)

print(data_trans)


five_of_kind = "{5,5}"
four_of_kind = "{4,4}"
full_house = ""
three_of_kind = ""
two_pair = ""
one_pair = ""
high_card = ""

CARDS_POWER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
HAND_TYPE_POWER = [
    "high_card",
    "1_pair",
    "2_pairs",
    "3_of_a_kind",
    "full_house",
    "4_of_a_kind",
    "5_of_a_kind",
]


class CamelCards:
    def __init__(self, card_power, hand_type_power):
        self.card_power_order = list(reversed(card_power))
        self.hand_type_power_order = hand_type_power
        # hand type, absolute order
        self.hands = []

    def get_card_power(self, card):
        return self.card_power_order.index(card)

    def get_hand_power(self, hand):
        absolute_order = self.get_absolute_order(hand)
        hand_type = self.get_hand_type(hand)
        hand_type_power = self.get_hand_type_power(hand_type)

        return [hand_type_power, hand_type, absolute_order]

    def get_hand_type(self, hand):
        card_counts = []
        for e in self.card_power_order:
            # print(e)
            card_counts.append(hand.count(e))

        # print(self.card_power_order)
        # print(card_counts)
        return self.get_hand_type_from_counts(card_counts)

    def get_hand_type_power(self, hand_type):
        return self.hand_type_power_order.index(hand_type)

    def get_absolute_order(self, hand):
        abs_order = ""
        for e in hand:
            # print(e, self.get_card_power(e))
            abs_order += f"{self.get_card_power(e):02d}"
        return abs_order

    def get_hand_type_from_counts(self, counts):
        c = counts
        if c.count(5) > 0:
            return "5_of_a_kind"
        elif c.count(4) > 0:
            return "4_of_a_kind"
        elif c.count(3) > 0 and c.count(2) > 0:
            return "full_house"
        elif c.count(3) > 0:
            return "3_of_a_kind"
        elif c.count(2) == 2:
            return "2_pairs"
        elif c.count(2) == 1:
            return "1_pair"
        else:
            return "high_card"

    def process_hands(self, hands):
        for e in hands:
            self.hands.append(self.get_hand_power(e) + [e])

        self.hands = sorted(self.hands, key=lambda x: (x[0], x[2]))

    def get_rank_of_hand(self, hand):
        for i in range(len(self.hands)):
            hand_curr = self.hands[i]
            # print("checking", hand_curr[3])
            if hand_curr[3] == hand:
                return i + 1
        return None


cc = CamelCards(CARDS_POWER, HAND_TYPE_POWER)
str_ = "AAAAA"
print(cc.get_absolute_order(str_))
print(cc.get_hand_power(str_))


hands = [e[0] for e in data_trans]
cc.process_hands(hands)
print(cc.hands)
hand = "KTJJT"
print("rank of hand:", hand, "is:", cc.get_rank_of_hand(hand))

# rank * bid
total_winnings = 0
for e in data_trans:
    hand = e[0]
    bid = e[1]
    total_winnings += cc.get_rank_of_hand(hand) * bid

print("total winnings:", total_winnings)
