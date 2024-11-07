def is_valid_assignment(graph, colors, region, color):
    for neighbor in graph[region]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, m, colors, region=0):
    if region == len(graph):
        return True

    for color in range(1, m + 1):
        if is_valid_assignment(graph, colors, region, color):
            colors[region] = color
            if map_coloring(graph, m, colors, region + 1):
                return True
            colors[region] = 0

    return False

def print_coloring(colors):
    print("Solution:")
    for i, color in enumerate(colors):
        print(f"Region {i + 1}: Color {color}")

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3
colors = [0] * len(graph)

if map_coloring(graph, m, colors):
    print_coloring(colors)
else:
    print("No solution exists")
