from Card import Card
import random


class Deck:

    suites = ['CLUB', 'SPADE', 'HEART', 'DIAMOND']
    values = [x for x in range(2, 15)]

    def __init__(self):
        self.cards = self.generate_cards()
        
    def has_cards(self):
        return self.cards

    def generate_cards(self):
        cards = []
        for suit in self.suites:
            for value in self.values:
                cards.append(Card(suit, value))

        random.shuffle(cards)
        return cards
    
    def get_card(self):
        if self.cards:
            return self.cards.pop()
