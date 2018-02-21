**Text-Based Hearts**

This is a command-line operated version of the game of Hearts. In it, you play against three computer players. 

The game starts when you run `python Game.py`. 

You are then asked to input the names of your opponents. 
The game then starts by displaying your hand and letting the player with the 2 of Clubs go first. 

Turn order then continues as expected. When it is your turn, you are presented with a list of cards it is legal for you to play.

You are then prompted to input an integer corresponding to the index of the card you want to play. 

Once the trick is complete, the game tells you who took the trick and then prints out your remaining hand, as well as the scores for all players.

The game continues until all cards have been played. At that point, the final scores are printed out.


This game currently uses a very basic AI. The Computer Players randomly select a legal card to play on their turns.
They do not promise to make any strategy other than that. 