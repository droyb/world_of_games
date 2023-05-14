import random
import time
from dataclasses import dataclass

from src.Games.BaseGame import BaseGame


@dataclass
class MemoryGame(BaseGame):
    MAX_NUMBER = 101

    def generate_sequence(self) -> list[int]:
        return [random.randint(1, self.MAX_NUMBER) for _ in range(self.difficulty)]

    def get_list_from_user(self) -> list[int]:
        print(f'Please choose {self.difficulty} numbers:')
        return [self.get_guess_from_user() for _ in range(self.difficulty)]

    def get_guess_from_user(self) -> int:
        while True:
            num = input(f'choose a number between 1 and {self.MAX_NUMBER}: ')
            if not num.isnumeric():
                print('Invalid number')
                continue
            num = int(num)
            if num < 1 or num > self.MAX_NUMBER:
                print('number not in range')
                continue
            return num

    @staticmethod
    def is_list_equal(list1: list, list2: list) -> bool:
        return all([x == y for (x, y) in zip(list1, list2)])

    def play(self) -> bool:
        sequence = self.generate_sequence()
        print('The numbers:', sequence, end='')
        time.sleep(0.7)
        print(end='\r')
        user_input = self.get_list_from_user()
        return self.is_list_equal(sequence, user_input)


if __name__ == '__main__':
    game = MemoryGame(difficulty=2)
    print(game.play())
