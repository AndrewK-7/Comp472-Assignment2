import time

from output_writer import OutputWriter
from algorithms.helper import Helper


class UniformCost:
    """
    This class is responsible for executing the "uniform cost" search algorithm on the provided puzzle instance.
    """

    def __init__(self, puzzle_num, puzzle, number_of_rows_per_puzzle, timeout):
        """
        Initialize this search algorithm object.
        :param puzzle_num: The puzzle number this is currently solving.
        :param puzzle: The initial-state of the puzzle.
        :param number_of_rows_per_puzzle: The number of rows that each puzzle will contain.
        :param timeout: The max number of seconds this algorithm has until it must be timed out.
        """
        # Set the puzzle's initial state
        self.puzzle = puzzle

        # Set the timeout time (in seconds)
        self.timeout = timeout

        # Set the helper class for use in performing the search
        self.helper = Helper(len(puzzle), number_of_rows_per_puzzle)

        # Define the output writer for this particular algorithm
        self.output_writer = OutputWriter(puzzle_num, "ucs")

        # Initialize our open and closed lists for the uniform cost search
        self.open_list = [Node(puzzle, None, 0, None)]
        self.closed_list = []
    # end: __init__

    def solve(self):
        """
        Solve the puzzle using the uniform cost search algorithm.
        :return: void
        """
        print("   Starting usc...", flush=True, end="\n")

        # We want to continue to loop until we have reached one of the following conditions:
        #   1. There are no more nodes in the open list (no solution found)
        #   2. We have reached the goal state (solution found)
        #   3. We have exceeded the timeout limit (no solution found)
        found_goal = False
        start_time = time.time()
        time_from_start = 0

        while not found_goal and len(self.open_list) > 0 and time_from_start < self.timeout:

            # Don't forget to update the time
            time_from_start = time.time() - start_time
        # end: while-loop

        print("   Done usc!", flush=True, end="\n")
    # end: solve
# end: class UniformCost


class Node:
    """
    A small class to house the common properties related to a node in our state tree.
    """

    def __init__(self, node_state, parent_state, total_cost_from_root, move_to_get_here_from_parent):
        """
        Define the node object.
        :param node_state: The state that this node contains.
        :param parent_state: The state of the parent node.
        :param total_cost_from_root: The total cost to get to this node from the root.
        :param move_to_get_here_from_parent: The type of move that was taken to reach this node.
        """
        self.state = node_state
        self.parent_state = parent_state
        self.total_cost_from_root = total_cost_from_root
        self.move = move_to_get_here_from_parent
    # end: __init__
# end: class Node
