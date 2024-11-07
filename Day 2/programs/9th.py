from itertools import permutations

def calculate_total_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]
    return total_distance

def travelling_salesman(graph):
    n = len(graph)
    nodes = list(range(n))
    min_path = None
    min_distance = float('inf')

    for perm in permutations(nodes[1:]):
        path = [0] + list(perm)
        distance = calculate_total_distance(graph, path)

        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance

graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

path, distance = travelling_salesman(graph)
print("Optimal path:", path)
print("Minimum distance:", distance)
