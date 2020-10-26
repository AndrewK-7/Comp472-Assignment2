from abc import ABC, abstractmethod
from Game import Game

class Search(ABC):

    def __init__(self, game: Game):
        self.game = game


    @abstractmethod
    def execute(self, game: Game):
        pass
    @abstractmethod
    def search(self, game: Game):
        pass