import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_pos = self.find_empty_position()
    
    def find_empty_position(self):
        for i, tile in enumerate(self.board):
            if tile == 0:
                return i
        return -1
    
    def is_goal(self):
        return self.board == list(range(1, 9)) + [0]

    def possible_moves(self):
        moves = []
        row, col = self.empty_pos // 3, self.empty_pos % 3
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_empty_pos = new_row * 3 + new_col
                new_board = self.board[:]
                new_board[self.empty_pos], new_board[new_empty_pos] = new_board[new_empty_pos], new_board[self.empty_pos]
                moves.append(PuzzleState(new_board, self.moves + 1, self))
        return moves
    
    def __lt__(self, other):
        return self.moves + self.manhattan_distance() < other.moves + other.manhattan_distance()
    
    def manhattan_distance(self):
        distance = 0
        for i, tile in enumerate(self.board):
            if tile != 0:
                correct_pos = tile - 1
                row_diff = abs(i // 3 - correct_pos // 3)
                col_diff = abs(i % 3 - correct_pos % 3)
                distance += row_diff + col_diff
        return distance

def solve_puzzle(initial_board):
    start_state = PuzzleState(initial_board)
    priority_queue = []
    visited = set()
    heapq.heappush(priority_queue, start_state)

    while priority_queue:
        current_state = heapq.heappop(priority_queue)

        if current_state.is_goal():
            return reconstruct_path(current_state)
        
        visited.add(tuple(current_state.board))
        
        for move in current_state.possible_moves():
            if tuple(move.board) not in visited:
                heapq.heappush(priority_queue, move)
    
    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]

initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = solve_puzzle(initial_board)

if solution:
    print("Solution found:")
    for step, board in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(board[i:i+3])
else:
    print("No solution found.")
