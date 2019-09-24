import random

HAND_SIZE = 5
DEBUG = 1
VERBOSE = 0


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(51, 1, -1):
            j = random.randint(0, i)
            # print(i, j)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.high_card = 0
        self.hand_counts = []
        self.pairs = 0
        self.trips = 0
        self.quads = 0
        self.is_flush = 0
        self.is_straight = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        i = 1
        for c in self.hand:
            print("[" + str(i) + "]")
            c.show()
            i += 1

    def discard(self, discards):
        for c in discards:
            tmp = self.hand.pop[c]

    def set_high_card(self):
        for c in self.hand:
            if c.value > self.high_card:
                self.high_card = c.value
            else:
                self.high_card = self.high_card

    def tally_hand(self):
        values = []
        _hand_counts = []
        for c in self.hand:
            values.append(c.value)

        values.sort()

        for v in values:
            if [v, values.count(v)] not in _hand_counts:
                _hand_counts.append([v, values.count(v)])

        # print(_hand_counts)

        self.hand_counts = _hand_counts

    def set_quads(self):
        for c in self.hand_counts:
            if c[1] == 4:
                self.quads = 1

    def set_trips(self):
        for c in self.hand_counts:
            if c[1] == 3:
                self.trips = 1

    def set_pairs(self):
        _pairs = 0
        for c in self.hand_counts:
            print(c[1])
            if c[1] == 2:
                _pairs = _pairs + 1

        print(_pairs)
        self.pairs = _pairs

    def set_flush(self):
        if self.hand[0].suit == self.hand[1].suit == self.hand[2].suit == self.hand[3].suit == self.hand[4].suit:
            self.is_flush = 1
        else:
            self.is_flush = 0

    def set_straight(self):
        self.hand.sort(key=lambda x: x.value)
        if self.hand[0].value == self.hand[1].value - 1 == self.hand[2].value - 2 == self.hand[3].value - 3 == self.hand[4].value - 4:
            self.is_straight = 1
        else:
            self.is_straight = 0

    def score_hand(self):
        self.tally_hand()
        self.set_flush()
        self.set_high_card()
        self.set_quads()
        self.set_straight()
        self.set_trips()
        self.set_pairs()

    def show_player(self):
        self.show_hand()
        if VERBOSE == 1:
            print("High Card: " + str(self.high_card))
            print(self.hand_counts)
            print("Flush? " + str(self.is_flush))
            print("Straight? " + str(self.is_straight))
            print("Four of a kind? " + str(self.quads))
            print("Three of a kind? " + str(self.trips))
            print("Pairs: " + str(self.pairs))


def main():
    deck = Deck()
    deck.shuffle()
#    print(len(deck.cards))
#    deck.show()
#    card = deck.draw_card()
#    card.show()

    player1 = Player('Ian')
    opponent1 = Player('Opponent')
    for i in range(0, HAND_SIZE):
        player1.draw(deck)

    print("Your hand: ")
    player1.show_player()

    discards = input("Discards (separated by spaces): ").split(" ")
    # print(discards)
    # print(len(discards))

    for d in discards:
        dc = player1.hand.pop(int(d) - 1)
        opponent1.hand.append(dc)

    # print(len(player1.hand))
    # print(len(opponent1.hand))


if __name__ == "__main__":
    main()