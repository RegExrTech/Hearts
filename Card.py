class Card:
    
    values = {
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "JACK",
        12: "QUEEN",
        13: "KING",
        14: "ACE"
    }
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return self.values[self.value] + " of " + self.suit + "s"

    def equals(self, card):
        return self.suit == card.suit and self.value == card.value
