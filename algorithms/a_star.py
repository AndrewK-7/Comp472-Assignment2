from output_writer import OutputWriter


class AStar:
    """
    This class is responsible for executing the "A*" search algorithm on the provided puzzle instance.
    """

    def __init__(self, puzzle_num, puzzle, heuristic_number):
        """
        Initialize this search algorithm object.
        :param puzzle_num: The puzzle number this is currently solving.
        :param puzzle: The initial-state of the puzzle.
        :param heuristic_number: The heuristic function to use (i.e. 1, or 2).
        """
        # Set the puzzle's initial state
        self.puzzle = puzzle
        self.heuristic = heuristic_number

        # Define the output writer for this algorithm
        self.output_writer = OutputWriter(puzzle_num, "astar", heuristic_number)
    # end: __init__

    def solve(self):
        """
        Solve the puzzle using the A* search algorithm.
        :return: void
        """
        print("   Starting astar-h%d..." % self.heuristic, flush=True, end="\n")

        # Execute algorithm here...

        print("   astar-h%d is done!" % self.heuristic, flush=True, end="\n")
    # end: solve
# end: class AStar
