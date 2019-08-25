import random

HAND_SIZE = 5


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
        for i in range(50, 1, -1):
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
        #self.is_flush = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for c in self.hand:
            c.show()

    def discard(self, discards):
        for c in discards:
            tmp = self.hand.pop[c]

    def set_high_card(self, hand):

        for c in hand:
            if c.value > self.high_card:
                self.high_card = c.value
            else:
                self.high_card = self.high_card

"""    def is_flush(self, hand):
        if hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit:
            return 1
        else:
            return 0
"""

def main():
    deck = Deck()
    deck.shuffle()
# print(len(deck.cards))
# deck.show()
# card = deck.draw_card()
# card.show()

    player1 = Player('Ian')
    for i in range(0, HAND_SIZE):
        player1.draw
    player1.show_hand()


if __name__ == "__main__":
    main()