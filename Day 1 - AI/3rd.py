from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])
    path = {}

    while queue:
        jug1, jug2 = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        if jug1 == target or jug2 == target:
            solution = []
            while (jug1, jug2) in path:
                solution.append((jug1, jug2))
                jug1, jug2 = path[(jug1, jug2)]
            solution.append((jug1, jug2))
            return solution[::-1]

        actions = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (min(jug1 + jug2, jug1_capacity), jug1 + jug2 - min(jug1 + jug2, jug1_capacity)),
            (jug1 + jug2 - min(jug1 + jug2, jug2_capacity), min(jug1 + jug2, jug2_capacity))
        ]

        for new_jug1, new_jug2 in actions:
            if (new_jug1, new_jug2) not in visited:
                queue.append((new_jug1, new_jug2))
                path[(new_jug1, new_jug2)] = (jug1, jug2)

    return None

jug1_capacity = 4
jug2_capacity = 3
target = 2

solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)

if solution:
    print("Solution steps:")
    for step, (jug1, jug2) in enumerate(solution):
        print(f"Step {step}: Jug1 = {jug1}L, Jug2 = {jug2}L")
else:
    print("No solution found.")
