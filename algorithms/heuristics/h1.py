

def h0(self, current_state):
    """
    Check h0
    if value of each index is different from goal state, add1.
    return minimum between h0 and h1 which is from two different goal.
    :param current_state: The current state of the puzzle.
    :return: h0 value
    """
    # Default the variable to be true
    is_goal = True

    h0 = 0
    h1 = 0

    # Check if the current state equals goal state 1
    for i in range(1, self.puzzle_length):
        if int(current_state[i - 1]) != i:
            h0 += 1
            is_goal = False

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
                    h1 += 1

                    # Increment our counter
                    counter += 1

                    # If we reached the last element, we want to set it to 0,
                    # since that is what the last element should be in goal-state-2
                    if counter == self.puzzle_length:
                        counter = 0
            # end: inner-for-loop
        # end: outer-for-loop
    # end: if

    return min(h0, h1)