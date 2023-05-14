from Games import MemoryGame, GuessGame, CurrencyRouletteGame, BaseGame
from Score import add_score
from Utils import screen_cleaner


def welcome(name):
    return f"""Hello {name} and welcome to the World of Games (WoG). 
Here you can find many cool games to play."""


def is_number_in_range(value, start, end):
    if not value.isnumeric():
        return False
    return start <= int(value) <= end


games = [MemoryGame, GuessGame, CurrencyRouletteGame]


def load_game():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    game_number = input()
    screen_cleaner()
    if not is_number_in_range(game_number, 1, 3):
        print("you can only choose game from 1 to 3")
        exit(0)

    print("Please choose game difficulty from 1 to 5: ", end="")
    difficulty = input()
    if not is_number_in_range(difficulty, 1, 5):
        print("you can only choose difficulty from 1 to 5")
        exit(0)
    difficulty = int(difficulty)
    game = games[int(game_number) - 1](difficulty=difficulty)
    won = game.play()
    if won:
        add_score(difficulty)
        print('You got it!')
    else:
        print('Loser!')
