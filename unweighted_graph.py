from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, u, v):
        # add nodes if they don't exist
        self.add_node(u)
        self.add_node(v)
        # add edge both ways for undirected graph
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)
    
    def remove_node(self, node):
        if node in self.graph:
            # remove all edges to this node
            for neighbors in self.graph.values():
                if node in neighbors:
                    neighbors.remove(node)
            del self.graph[node]
    
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def bfs(self, start, goal):
        visited, q = set(), deque([start])
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                if node == goal:
                    print(f"\n{goal} reached")
                    return
                q.extend(n for n in self.graph[node] if n not in visited)
    
    def dfs(self, node, goal, visited=None):
        if visited is None:
            visited = set()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            if node == goal:
                print(f"\n{goal} reached")
                return
            for neighbor in self.graph[node]:
                self.dfs(neighbor, goal, visited)

if __name__ == "__main__":
    # create graph and add edges
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    for u, v in edges:
        g.add_edge(u, v)
    
    print("BFS from 0 to 3:")
    g.bfs(0, 3)
    
    print("\nDFS from 0 to 3:")
    g.dfs(0, 3)
