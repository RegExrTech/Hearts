from Deck import Deck
from Player import Player
from Card import Card


class Game:

    def __init__(self):
        self.deck = Deck()
        self.players = self.set_players()
        self.starting_player_index = 0
        self.leading_card = None
        self.hearts_is_broken = False
        self.cards_played = []

    def deal_cards(self):
        while self.deck.has_cards():
            for player in self.players:
                self.give_card(player, self.deck)
        for player in self.players:
            player.sort_cards()

    def give_card(self, player, deck):
        card = deck.get_card()
        player.take_card(card)

    def set_players(self):
        players = [Player()]
        for i in range(3):
            name = input("Please enter a player name: ")
            players.append(Player(name))
        return players

    def find_starting_player(self):
        for i in range(len(self.players)):
            player = self.players[i]
            if player.has(Card('CLUB', 2)):
                return i
            
    def play_round(self):
        for i in range(4):
            player = self.players[(self.starting_player_index + i) % 4]
            played_card = player.make_move(self.leading_card, self.hearts_is_broken)
            print(player.name + " played " + str(played_card))
            if i == 0:
                self.leading_card = played_card
            if played_card.suit == 'HEART':
                self.hearts_is_broken = True
            self.cards_played.append(played_card)
        highest_value = 0
        highest_card = None
        for card in self.cards_played:
            if card.suit == self.leading_card.suit and card.value > highest_value:
                highest_card = card
                highest_value = card.value
        taking_player = self.players[((self.starting_player_index + self.cards_played.index(highest_card)) % 4)]
        print(taking_player.name + " took the trick.")
        for card in self.cards_played:
            if card.suit == "HEART":
                taking_player.points += 1
            if card.suit == "SPADE" and card.value == 12:
                taking_player.points += 13
        print("\n=== CURRENT STANDINGS ===")
        for player in self.players:
            print(player)
        print("")
        self.starting_player_index = self.players.index(taking_player)
        self.leading_card = None
        self.cards_played = []

    def play_game(self):
        self.deal_cards()
        self.starting_player_index = self.find_starting_player()
        print("Your starting hand: " + str(self.players[1].cards))
        while self.players[-1].cards:
            self.play_round()
        for player in self.players:
            if player.points == 26:
                for player_2 in self.players:
                    if player_2.name == player.name:
                        player.score = 0
                    else:
                        player.score = 26
                break
        for player in self.players:
            print(player)


if __name__ == '__main__':
    game = Game()
    game.play_game()
