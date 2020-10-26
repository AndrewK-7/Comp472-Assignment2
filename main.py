
from Game import Game
from Astar import Astar


def main():
    print("a")


    for key, element in enumerate(loader("input.txt")):
        print(element)
        game = Game(element)

       # greedy = greedy(game)
       # greedy.search()

       # uniform = uniform(game)
       # uniform.search()

        astar = Astar(game)
        astar.search()

def loader(input_file):
    input_list = []
    with open(input_file) as file:
        for line in file:
            input_list.append(line.strip('\n').split( " "))
    return input_list

if __name__ == "__main__":
    main()