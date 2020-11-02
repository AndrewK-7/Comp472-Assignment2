from output_writer import OutputWriter


class UniformCost:
    """
    This class is responsible for executing the "uniform cost" search algorithm on the provided puzzle instance.
    """

    def __init__(self, puzzle_num, puzzle):
        """
        Initialize this search algorithm object.
        :param puzzle_num: The puzzle number this is currently solving.
        :param puzzle: The initial-state of the puzzle.
        """
        # Set the puzzle's initial state
        self.puzzle = puzzle

        # Define the output writer for this algorithm
        self.output_writer = OutputWriter(puzzle_num, "ucs")
    # end: __init__

    def solve(self):
        """
        Solve the puzzle using the uniform cost search algorithm.
        :return: void
        """
        print("   Starting usc...", flush=True, end="\n")

        # Execute algorithm here...

        print("   usc is done!", flush=True, end="\n")

    # end: solve
# end: class UniformCost
