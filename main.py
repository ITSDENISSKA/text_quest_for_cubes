from game import Game
from player import Player

if __name__ == "__main__":
    player = Player()
    game = Game(player)
    game.start_game()
