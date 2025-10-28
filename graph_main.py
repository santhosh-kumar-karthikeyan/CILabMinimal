from collections import deque #Using deque for O(1) popping from the front and insertion into the last

class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    def del_node(self,node):
        for n in self.graph:
            if node in n:
                self.graph[n].remove(node)
        self.graph.pop(node)
    def add_edge(self, node1, node2):
        if node1 not in self.graph[node2]:
            self.graph[node2].append(node1)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
    def del_edge(self,node1, node2):
        if node1 in self.graph[node2]:
            self.graph[node2].remove(node1)
        if node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
    def bfs(self, start, goal):
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
                q.extend(neigh for neigh in self.graph[n] if neigh not in visited)
    
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
    graph_controller.add_edge(1,2)
    graph_controller.add_edge(1,3)
    graph_controller.add_edge(2,4)
    graph_controller.add_edge(2,5)
    graph_controller.add_edge(3,6)
    graph_controller.bfs(5,4)
    print(graph_controller.graph)