import queue

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def size(self):
        size_x = len(self.graph)
        size_y = len(self.graph[0])
        return(size_x, size_y)

    def neighbors(self, location=(0,0)):
        relative_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for i, j in relative_neighbors:
            neighbor = location[0] + i, location[1] + j
            if 0 <= neighbor[0] < self.size()[0] and 0 <= neighbor[1] < self.size()[1]:
                neighbors.append(neighbor)
        return neighbors

def breadth_first(graph, start, goal):
    frontier = queue.Queue()
    frontier.put(start )
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            print(next)
            if next not in visited:
                frontier.put(next)
                visited[next] = True




grid_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

grid_input = [[0, 0, 0, 0],
			  [0, 0, 0, 0],
			  [0, 0, 0, 0],
			  [0, 0, 0, 0],
			  [0, 0, 1, 1]] 

graph = Graph(grid_input)
breadth_first(graph, (0,0), (1,1))