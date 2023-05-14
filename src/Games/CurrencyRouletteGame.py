import random
from dataclasses import dataclass
import py_currency_converter

from src.Games.BaseGame import BaseGame


@dataclass
class CurrencyRouletteGame(BaseGame):

    def get_money_interval(self, usd_amount: int) -> tuple[float, float]:
        res = py_currency_converter.convert(base='USD', amount=usd_amount, to=["ILS"])
        total = res['ILS']
        diff = 5 - self.difficulty
        return (total - diff), (total + diff)

    @staticmethod
    def get_guess_from_user() -> int:
        while True:
            num = input('guess the amount in ILS: ')
            if not num.isnumeric():
                print('Invalid number')
                continue
            return int(num)

    def play(self):
        usd_amount = random.randint(1, 100)
        print(f'The value in USD is: {usd_amount}')
        guess = self.get_guess_from_user()
        min_value, max_value = self.get_money_interval(usd_amount)
        return min_value <= guess <= max_value


if __name__ == '__main__':
    game = CurrencyRouletteGame(difficulty=2)
    print(game.play())
