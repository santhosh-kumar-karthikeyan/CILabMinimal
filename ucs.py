import heapq

def ucs(graph, start, goal):
    pq, visited = [(0, start)], set()
    while pq:
        c, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            print(f"{node} : {c}", end = ' ')
            if node == goal:
                print()
                print(f"{goal} reached with cost {c}")
                return
            for neigh, cost  in graph[node].items():
                if neigh not in visited:
                    heapq.heappush(pq, (cost + c, neigh))

if __name__ == "__main__":
    graph_weighted = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    ucs(graph_weighted, 'A', 'D')
