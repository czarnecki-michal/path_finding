class Grid:
    def __init__(self, grid):
        self.grid = grid

    def size(self):
        size_x = len(self.grid)
        size_y = len(self.grid[0])
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
        for row in self.grid:
            print(row)
        print("\n")

    def cost(self, from_node, to_node):
        return self.grid[to_node[0]][to_node[1]]
