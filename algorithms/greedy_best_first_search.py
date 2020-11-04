from output_writer import OutputWriter
from algorithms.helper import Helper


class GreedyBestFirstSearch:
    """
    This class is responsible for executing the "greedy-best-first-search" search algorithm on the
    provided puzzle instance.
    """

    def __init__(self, puzzle_num, puzzle, heuristic_number, number_of_rows_per_puzzle):
        """
        Initialize this search algorithm object.
        :param puzzle_num: The puzzle number this is currently solving.
        :param puzzle: The initial-state of the puzzle.
        :param heuristic_number: The heuristic function to use (i.e. 1, or 2).
        :param number_of_rows_per_puzzle: The number of rows that each puzzle will contain.
        """
        # Set the puzzle's initial state
        self.puzzle = puzzle
        self.heuristic = heuristic_number

        # Set the helper class for use in solving the search
        self.helper = Helper(len(puzzle), number_of_rows_per_puzzle)

        # Define the output writer for this algorithm
        self.output_writer = OutputWriter(puzzle_num, "gbfs", heuristic_number)
    # end: __init__

    def solve(self):
        """
        Solve the puzzle using the greedy best first search search algorithm.
        :return: void
        """
        print("   Starting gbfs-h%d..." % self.heuristic, flush=True, end="\n")

        # Execute algorithm here...

        print("   gbfs-h%d is done!" % self.heuristic, flush=True, end="\n")
    # end: solve
# end: class GreedyBestFirstSearch
