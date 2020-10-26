from Game import Game
from queue import PriorityQueue
from Search import Search

QueuList= PriorityQueue()

class Uniform(Search):
    def __init__(self, game: Game):
        super().__init__(game)
        self.game.H1()

    def search(self):
        print("search")
    def execute(self):
        return 0

