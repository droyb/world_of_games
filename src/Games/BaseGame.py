from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseGame(ABC):
    difficulty: int

    @abstractmethod
    def play(self) -> bool:
        pass
