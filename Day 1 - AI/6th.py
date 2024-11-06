class VacuumCleaner:
    def __init__(self, initial_state):
        self.state = initial_state
        self.position = 'A'  # Starting position

    def display_state(self):
        print(f"Room A: {'Dirty' if self.state['A'] else 'Clean'}, Room B: {'Dirty' if self.state['B'] else 'Clean'}")

    def clean(self):
        steps = 0
        while self.state['A'] or self.state['B']:
            if self.state[self.position]:  
                print(f"Position: {self.position} - Dirty. Cleaning...")
                self.state[self.position] = 0  
                steps += 1
                print(f"Position: {self.position} cleaned.")

            if self.position == 'A' and self.state['B']:  
                self.position = 'B'
                print("Moving to Room B")
            elif self.position == 'B' and self.state['A']:
                self.position = 'A'
                print("Moving to Room A")

        print(f"All rooms are clean! Total steps taken: {steps}")

# Initial state: 1 for dirty, 0 for clean
initial_state = {'A': 1, 'B': 1}  
vacuum = VacuumCleaner(initial_state)

print("Initial room states:")
vacuum.display_state()
vacuum.clean()
