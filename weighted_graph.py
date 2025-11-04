import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}
    
    def add_edge(self, u, v, weight):
        # add nodes if they don't exist
        self.add_node(u)
        self.add_node(v)
        # add weighted edge both ways for undirected graph
        self.graph[u][v] = weight
        self.graph[v][u] = weight
    
    def remove_node(self, node):
        if node in self.graph:
            # remove all edges to this node
            for neighbors in self.graph.values():
                neighbors.pop(node, None)
            del self.graph[node]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            self.graph[u].pop(v, None)
        if v in self.graph:
            self.graph[v].pop(u, None)
    
    def ucs(self, start, goal):
        pq, visited = [(0, start)], set()
        while pq:
            cost, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                print(f"{node}:{cost}", end=' ')
                if node == goal:
                    print(f"\n{goal} reached with cost {cost}")
                    return
                for neighbor, weight in self.graph[node].items():
                    if neighbor not in visited:
                        heapq.heappush(pq, (cost + weight, neighbor))
    
    def astar(self, start, goal, heuristic):
        pq, visited = [(heuristic[start], 0, start)], set()
        while pq:
            f, g, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                if node == goal:
                    print(f"\n{goal} reached with cost {g}")
                    return
                for neighbor, weight in self.graph[node].items():
                    if neighbor not in visited:
                        h = heuristic[neighbor]
                        heapq.heappush(pq, (h + g + weight, g + weight, neighbor))

if __name__ == "__main__":
    # create weighted graph and add edges
    g = WeightedGraph()
    g.add_edge('A','B',1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    ####       A
    #      1 /   \ 4
    #       B ___ C 
    #    5 /   2 
    #     D
    print("UCS from A to D:")
    g.ucs('A', 'D')
    
    # heuristic values for A* (estimate to goal D)
    heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    print("\nA* from A to D:")
    g.astar('A', 'D', heuristic)
    
