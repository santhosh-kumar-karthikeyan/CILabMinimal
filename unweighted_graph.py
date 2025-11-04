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
    graph_controller = Graph()
    for node_i in range(1,7):
        graph_controller.add_node(node_i) #Creates nodes 1 .. 6
    # Following is the structure of the graph being constructed
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    # Idhelam varanjadhuku follow pannunga da 
    graph_controller.add_edge(1,2)
    graph_controller.add_edge(1,3)
    graph_controller.add_edge(2,4)
    graph_controller.add_edge(2,5)
    graph_controller.add_edge(3,6)
    graph_controller.bfs(5,4)

    print(graph_controller.graph)
