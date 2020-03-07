from Game import Game
from Player import Human, Bot
print("Welcome to The Open-Closed Game")

while(True):
    human = Human("You")
    bot = Bot("Bot")
    game = Game(human, bot)
    game.play()
    if (not game.check_play_again()): break