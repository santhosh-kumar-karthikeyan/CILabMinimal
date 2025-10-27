def dfs(graph, node, goal, visited = None):
    if visited is None: visited = set()
    if node not in visited:
        visited.add(node)
        print(node, end = ' ')
        if node == goal:
            print()
            print(f"{goal} reached")
            return
        for neigh in graph[node]:
            dfs(graph, neigh, goal, visited)

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    dfs(graph, 0, 3)
