import queue

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

# grid_input = [[0, 0, 0, 0],
#               [0, 0, 0, 0],
#               [0, 0, 0, 0],
#               [0, 0, 0, 0],
#               [0, 0, 1, 1]] 


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

    def update(self, location=(0,0)):
        self.graph[location[0]][location[1]] = 9
    
    def show(self):
        for row in self.graph:
            print(row)
        print("\n")

def breadth_first(graph, start, goal):
    frontier = queue.Queue()
    frontier.put(start )
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from

def reconstruct_path(came_from, start, goal):   
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

def print_grid(grid, path):
    grid1 = grid.graph[:]
    try:
        for list in grid1:
            for i, x in enumerate(list):
                if x == 1:
                    list[i] = "■"
                if x == 0:
                    list[i] = " "
        for x, y in path:
            grid1[x][y] = "·"
        start_x, start_y = path[0]
        goal_x, goal_y = path[-1]
        grid1[start_x][start_y] = "A"
        grid1[goal_x][goal_y] = "B"
        for i in grid1:
            print(" ".join(i))
    except:
        print("Brak przejścia")


graph = Graph(grid_input)
came_from = breadth_first(graph, (0,0), (12,12))
path = reconstruct_path(came_from, (0,0), (12,12))

print_grid(graph, path)