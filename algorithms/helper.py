class Helper:
    """
    Class contains some common helper functions that the search algorithms will need to use.
    """

    def __init__(self, size_of_puzzle, number_of_rows=2):
        """
        Initialize the helper object.
        :param size_of_puzzle: The size of the puzzle (how many cells are there in all).
        :param number_of_rows: The number of rows in the puzzle.
        """
        self.puzzle_length = size_of_puzzle
        self.number_of_rows = number_of_rows
        self.puzzle_width = int(size_of_puzzle / number_of_rows)

    # end: __init__

    def is_goal_state(self, current_state):
        """
        Check if the current state is one of the goal states.
        There are two goal states, defined by the assignment in section 1.1 on page 1.
        :param current_state: The current state of the puzzle.
        :return: boolean, True if the current state is in fact a goal state, False otherwise.
        """
        # Default the variable to be true
        is_goal = True

        # Check if the current state equals goal state 1
        for i in range(1, self.puzzle_length - 1):
            if int(current_state[i - 1]) != i:
                is_goal = False
                break
        # end: for-loop

        # Only check if the current state equals goal state 2
        # if we didn't already determine it was goal state 1
        if not is_goal:
            is_goal = True  # Reset the value
            counter = 1
            # Check if the current state equals goal state 2
            for j in range(self.puzzle_width):
                for i in range(self.number_of_rows):
                    if int(current_state[i * self.puzzle_width + j]) != counter:
                        is_goal = False
                        break
                    else:
                        # Increment our counter
                        counter += 1

                        # If we reached the last element, we want to set it to 0,
                        # since that is what the last element should be in goal-state-2
                        if counter == self.puzzle_length:
                            counter = 0
                # end: inner-for-loop
            # end: outer-for-loop
        # end: if

        return is_goal

    # end: is_goal_state

    def move_up(self, current_state):
        """
        A "regular move", which involves moving the '0' tile up one cell.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # If the index of the '0' tile is in the top-row then we cannot do the action
        if index in range(0, self.puzzle_width - 1):
            return 0

        # Else, we can move the '0' tile up by one and swap it with the tile that was there
        else:
            # To find the index of the tile 'directly above' the '0', we can simply subtract the '0' index by the width
            # of the puzzle
            index_to_swap = index - self.puzzle_width

            # Double check that we are not below zero
            if index_to_swap < 0:
                return 0

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'move-up' is 1
        return 1

    # end: move_up

    def move_down(self, current_state):
        """
        A "regular move", which involves moving the '0' tile down one cell.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # If the index of the '0' tile is in the bottom-row then we cannot do the action
        if index in range(self.puzzle_length - self.puzzle_width, self.puzzle_length - 1):
            return 0

        # Else, we can move the '0' tile down by one and swap it with the tile that was there
        else:
            # To find the index of the tile 'directly below' the '0', we can simply add the '0' index by the width
            # of the puzzle
            index_to_swap = index + self.puzzle_width

            # Double check that we are not above the length
            if index_to_swap >= self.puzzle_length:
                return 0

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'move-down' is 1
        return 1

    # end: move_down

    def move_left(self, current_state):
        """
        A "regular move", which involves moving the '0' tile left one cell.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # Get all of the indices that belong to the left-most tiles
        left_most_indices = [i * self.puzzle_width for i in range(0, self.number_of_rows)]

        # If the index of the '0' tile is in any of the left-most positions, then we cannot do the action
        if index in left_most_indices:
            return 0

        # Else, we can move the '0' tile left by one and swap it with the tile that was there
        else:
            # To find the index of the tile 'directly to the left' of the '0', we can simply subtract the '0' index by 1
            index_to_swap = index - 1

            # Double check that we are not below 0
            if index_to_swap < 0:
                return 0

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'move-left' is 1
        return 1

    # end: move_left

    def move_right(self, current_state):
        """
        A "regular move", which involves moving the '0' tile right one cell.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # Get all of the indices that belong to the right-most tiles
        right_most_indices = [(i * self.puzzle_width) + self.puzzle_width - 1 for i in range(0, self.number_of_rows)]

        # If the index of the '0' tile is in any of the right-most positions, then we cannot do the action
        if index in right_most_indices:
            return 0

        # Else, we can move the '0' tile right by one and swap it with the tile that was there
        else:
            # To find the index of the tile 'directly to the right' of the '0', we can simply add to the '0' index by 1
            index_to_swap = index + 1

            # Double check that we are not above the length
            if index_to_swap >= self.puzzle_length:
                return 0

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'move-right' is 1
        return 1

    # end: move_right

    def wrap(self, current_state):
        """
        A "wrapping move", which involves moving the '0' tile from one of the corner positions across to the opposite
        corner position (not diagonally).
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # Define the indices that the '0' tile is allowed to be in for a wrapping move (all four corners)
        allowed_indices = [0, self.puzzle_width - 1, self.puzzle_length - self.puzzle_width, self.puzzle_length - 1]

        # If the index of the '0' tile is not in any of the allowed positions, then we cannot do the action
        if index not in allowed_indices:
            return 0

        # Else, we can move the '0' tile to the other side of the grid
        else:
            # We need to find the opposite position of the '0' tile
            index_to_swap = index

            # If the '0' tile is in the top-left corner, then we need to switch it with the tile in the top-right corner
            if index == 0:
                index_to_swap = self.puzzle_width - 1

            # If the '0' tile is in the top-right corner, then we need to switch it with the tile in the top-left corner
            elif index == self.puzzle_width - 1:
                index_to_swap = 0

            # If the tile is in the bottom-left corner, then we need to switch with the tile in the bottom-right corner
            elif index == self.puzzle_length - self.puzzle_width:
                index_to_swap = self.puzzle_length - 1

            # If the tile is in the bottom-right corner, then we need to switch with the tile in the bottom-left corner
            elif index == self.puzzle_length - 1:
                index_to_swap = self.puzzle_length - self.puzzle_width

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'wrap' is 2
        return 2

    # end: wrap

    def diagonal_adjacent(self, current_state):
        """
        A "diagonal move", which involves moving the '0' tile from one of the corner positions to diagonally adjacent.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # Define the indices that the '0' tile is allowed to be in for a diagonal move (all four corners)
        allowed_indices = [0, self.puzzle_width - 1, self.puzzle_length - self.puzzle_width, self.puzzle_length - 1]

        # If the index of the '0' tile is not in any of the allowed positions, then we cannot do the action
        if index not in allowed_indices:
            return 0

        # Else, we can move the '0' tile to the other side of the grid
        else:
            # We need to find the adjacent-diagonal position of the '0' tile
            index_to_swap = index

            # If the '0' tile is in the top-left corner, then we need to switch it with the tile +1 row and +1 column
            if index == 0:
                index_to_swap = index + self.puzzle_width + 1

            # If the '0' tile is in the top-right corner, then we need to switch it with the tile +1 row and -1 column
            elif index == self.puzzle_width - 1:
                index_to_swap = index + self.puzzle_width - 1

            # If the tile is in the bottom-left corner, then we need to switch with the tile -1 row and +1 column
            elif index == self.puzzle_length - self.puzzle_width:
                index_to_swap = index - self.puzzle_width + 1

            # If the tile is in the bottom-right corner, then we need to switch with the tile -1 row and -1 column
            elif index == self.puzzle_length - 1:
                index_to_swap = index - self.puzzle_width - 1

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'diagonal' move is 3
        return 3

    # end: diagonal_adjacent

    def diagonal_across(self, current_state):
        """
        A "diagonal move", which involves moving the '0' tile from one of the corner positions to diagonally across.
        :param current_state: The current configuration of the puzzle. NOTE: We are modifying the array by reference.
        :return: The cost of performing this move.
        """
        # Find the index of the '0' tile
        index = current_state.index('0')

        # Define the indices that the '0' tile is allowed to be in for a diagonal move (all four corners)
        allowed_indices = [0, self.puzzle_width - 1, self.puzzle_length - self.puzzle_width, self.puzzle_length - 1]

        # If the index of the '0' tile is not in any of the allowed positions, then we cannot do the action
        if index not in allowed_indices:
            return 0

        # Else, we can move the '0' tile to the other side of the grid
        else:
            # We need to find the diagonal-across position of the '0' tile
            index_to_swap = index

            # If the '0' tile is in the top-left corner, then we need to switch it with the bottom-right corner
            if index == 0:
                index_to_swap = self.puzzle_length - 1

            # If the '0' tile is in the top-right corner, then we need to switch it with the bottom-left corner
            elif index == self.puzzle_width - 1:
                index_to_swap = self.puzzle_length - self.puzzle_width

            # If the '0' tile is in the bottom-left corner, then we need to switch it with the top-right corner
            elif index == self.puzzle_length - self.puzzle_width:
                index_to_swap = self.puzzle_width - 1

            # If the '0' tile is in the bottom-right corner, then we need to switch it with the top-left corner
            elif index == self.puzzle_length - 1:
                index_to_swap = 0

            # Swap the '0' tile with the other index
            current_state[index] = current_state[index_to_swap]
            current_state[index_to_swap] = '0'
        # end: if-else

        # If everything went well, then the cost of a 'diagonal' move is 3
        return 3
    # end: diagonal_across
# end: class Helper
