from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, moves):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.moves = moves

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.cannibals > self.missionaries:
            return False
        if (3 - self.missionaries) > 0 and (3 - self.cannibals) > (3 - self.missionaries):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_next_states(self):
        next_states = []
        if self.boat == 1:
            next_states.append(State(self.missionaries - 2, self.cannibals, 0, self.moves + [(2, 0)]))
            next_states.append(State(self.missionaries, self.cannibals - 2, 0, self.moves + [(0, 2)]))
            next_states.append(State(self.missionaries - 1, self.cannibals - 1, 0, self.moves + [(1, 1)]))
            next_states.append(State(self.missionaries - 1, self.cannibals, 0, self.moves + [(1, 0)]))
            next_states.append(State(self.missionaries, self.cannibals - 1, 0, self.moves + [(0, 1)]))
        else:
            next_states.append(State(self.missionaries + 2, self.cannibals, 1, self.moves + [(-2, 0)]))
            next_states.append(State(self.missionaries, self.cannibals + 2, 1, self.moves + [(0, -2)]))
            next_states.append(State(self.missionaries + 1, self.cannibals + 1, 1, self.moves + [(-1, -1)]))
            next_states.append(State(self.missionaries + 1, self.cannibals, 1, self.moves + [(-1, 0)]))
            next_states.append(State(self.missionaries, self.cannibals + 1, 1, self.moves + [(0, -1)]))
        return [state for state in next_states if state.is_valid()]

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 1, [])
    queue = deque([initial_state])
    visited = set()
    visited.add((3, 3, 1))

    while queue:
        state = queue.popleft()
        
        if state.is_goal():
            return state.moves

        for next_state in state.get_next_states():
            state_tuple = (next_state.missionaries, next_state.cannibals, next_state.boat)
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append(next_state)

    return None

solution = solve_missionaries_cannibals()

if solution:
    print("Solution steps (Missionaries, Cannibals moved):")
    for step, move in enumerate(solution):
        print(f"Step {step + 1}: Move {move[0]} missionaries and {move[1]} cannibals")
else:
    print("No solution found.")
