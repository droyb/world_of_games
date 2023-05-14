from dataclasses import dataclass
import random

from src.Games.BaseGame import BaseGame


@dataclass
class GuessGame(BaseGame):

    def play(self) -> bool:
        secret_number = self.generate_number()
        guess = self.get_guess_from_user()
        return self.compare_results(guess, secret_number)

    def generate_number(self) -> int:
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self) -> int:
        while True:
            num = input(f'choose a number between 1 and {self.difficulty}: ')
            if not num.isnumeric():
                print('Invalid number')
                continue
            num = int(num)
            if num < 1 or num > self.difficulty:
                print('number not in range')
                continue
            return num

    @staticmethod
    def compare_results(guess: int, secret: int) -> bool:
        return guess == secret


if __name__ == '__main__':
    game = GuessGame(difficulty=5)
    result = game.play()
    print(result)
