from collections import deque

def bfs(graph, start, goal):
    visited = set()
    q = deque([start])
    while q:
        n = q.popleft()
        if n not in visited:
            visited.add(n)
            print(n, end = ' ')
            if n == goal:
                print()
                print(f"{goal} reached")
                return
            q.extend(neigh for neigh in graph[n] if neigh not in visited)

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }   
    bfs(graph, 0, 3)
