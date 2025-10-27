import heapq

def astar(graph, start, goal, heuristic):
    pq, visited = [(heuristic[start], 0, start)], set()
    while pq:
        f, g, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            print(node, end = ' ')
            if node == goal:
                print()
                print(f"{goal} reached with cost {g}")
                return
            for neigh, cost in graph[node].items():
                if neigh not in visited:
                    heapq.heappush(pq, (heuristic[neigh] + g + cost, g + cost, neigh))

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Heuristic estimate of cost from each node to goal 'D'
    heuristic = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    astar(graph, 'A', 'D', heuristic)

