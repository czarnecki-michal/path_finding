import grid
from pathfinding_algorithms import BreadthFirst, Dijkstra, GreedyBFS, Astar

# 1 - passable node, but higher movement cost,
# 2 - impassable node - wall

grid_input = [[0, 0, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 2, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

grid = grid.Grid(grid_input)
pathfinder = Astar(grid)
pathfinder.solve(start=(1,1), goal=(10,10))
pathfinder.show_result()