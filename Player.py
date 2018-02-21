import random
from Card import Card


class Player:

    def __init__(self, name="You"):
        self.cards = []
        self.name = name
        self.points = 0

    def __repr__(self):
        if self.name == 'You':
            return self.name + " - " + str(self.cards) + "\nYou have " + str(self.points) + " points."
        return self.name + " has " + str(self.points) + " points."

    def sort_cards(self):
        self.cards = sorted(self.cards, key=lambda card: (card.suit, card.value))

    def has(self, start_card):
        for card in self.cards:
            if card.equals(start_card):
                return True
        return False

    def make_move(self, leading_card, hearts_is_broken):
        possible_cards = []
        if self.has(Card('CLUB', 2)):
            possible_cards.append(self.cards[0])
        else:
            if leading_card == None:
                leading_card = Card('NONE', -1)
            for card in self.cards:
                if card.suit == leading_card.suit:
                    possible_cards.append(card)
            if not possible_cards:
                for card in self.cards:
                    if card.suit == 'HEART':
                        # Can't lead with hearts unless hearts has already been broken and this is not the first trick
                        if leading_card.suit == "NONE" or (leading_card.suit == 'CLUB' and leading_card.value == 2):
                            if hearts_is_broken:
                                possible_cards.append(card)
                        else:
                            possible_cards.append(card)
                    else:
                        possible_cards.append(card)
        while True:
            if self.name == "You":
                print(possible_cards)
                user = int(input(">> "))
            else:
                user = random.randint(0, len(possible_cards)-1)
            try:
                card = possible_cards[user]
                break
            except:
                print("Not a valid choice. Try again.")
        self.cards.remove(card)
        return card

    def take_card(self, card):
        self.cards.append(card)
