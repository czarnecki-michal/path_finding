class Grid:
    def __init__(self, grid):
        self.grid = grid

    def size(self):
        '''Returns size of input grid'''

        size_x = len(self.grid)
        size_y = len(self.grid[0])
        return(size_x, size_y)

    def neighbors(self, location=(0,0)):
        '''Returns coordinates of neighbors for specified node'''

        relative_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)] #coordinates of neighbors relative to chosen node
        neighbors = []
        for i, j in relative_neighbors:
            neighbor = location[0] + i, location[1] + j
            if 0 <= neighbor[0] < self.size()[0] and 0 <= neighbor[1] < self.size()[1]: #to neighbors list are added only nodes which fit in bounding box of input grid
                neighbors.append(neighbor)
        return neighbors

    def cost(self, to_node):
        '''Returns cost of movement to node'''

        return self.grid[to_node[0]][to_node[1]]
