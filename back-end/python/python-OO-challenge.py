#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self):
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def split_cards(self):
        return (self.allcards[:26], self.allcards[26:])

    def shuffle_cards(self):
        shuffle(self.allcards)

    def deal_cards(self):
        self.shuffle_cards()
        return self.split_cards()


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, cards):
        self.cards.extend(cards)

    def remove(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        card = self.hand.remove()
        print('{} played {}'.format(self.name, card))
        return card

    def draw_war_cards(self):
        count = len(self.hand.cards)
        if count < 3:
            return [self.hand.remove() for i in range(len(self.hand.cards))]
        else:
            return [self.hand.remove() for i in range(3)]

    def has_cards(self):
        return len(self.hand.cards) > 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck = Deck()
hand1, hand2 = deck.deal_cards()

human = Player(input('What is your name? '), Hand(hand1))
computer = Player('Computer', Hand(hand2))

print('Let the games begin...')
rounds = 0
war_count = 0

while(human.has_cards() and computer.has_cards()):
    rounds++




# Use the 3 classes along with some logic to play a game of war!
