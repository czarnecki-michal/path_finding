from queue import Queue
from queue import PriorityQueue

class Pathfinder:
    def __init__(self, grid):
        self.grid = grid
        self.path = []

    def reconstruct_path(self, came_from, start, goal):   
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path
    
    def calculate_distance(self, from_node=(0,0), to_node=(0,0)):
        (x1, y1) = from_node
        (x2, y2) = to_node
        return abs(x1 - x2) + abs(y1 - y2)

    def show_result(self):
        grid1 = self.grid.grid[:]
        try:
            for x, y in self.path:
                grid1[x][y] = "·"
            for list in grid1:
                for i, x in enumerate(list):
                    if x == 1:
                        list[i] = "▥"
                    if x == 0:
                        list[i] = " "
                    if x == 2:
                        list[i] = "▦"
            start_x, start_y = self.path[0]
            goal_x, goal_y = self.path[-1]
            grid1[start_x][start_y] = "A"
            grid1[goal_x][goal_y] = "B"
            for i in grid1:
                print(" ".join(i))
        except:
            print("Brak przejścia")

class BreadthFirst(Pathfinder):
    def solve(self, start=(0,0), goal=(0,0)):
        frontier = Queue() #a ring expanding in all directions
        frontier.put(start)
        visited = {} #visited nodes
        visited[start] = None

        while not frontier.empty():
            current = frontier.get() #gets current node and removes it from frontier
            if current == goal:
                break
            for next in self.grid.neighbors(current):
                if next not in visited:
                    frontier.put(next)
                    visited[next] = current
        
        self.path = self.reconstruct_path(visited, start, goal)
        return self.path

class GreedyBFS(Pathfinder):
    def solve(self, start=(0,0), goal=(0,0)):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        visited = {}
        visited[start] = None

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break        
            for next in self.grid.neighbors(current):
                if next not in visited:
                    priority = self.calculate_distance(goal, next)
                    frontier.put(next, priority)
                    visited[next] = current

        self.path = self.reconstruct_path(visited, start, goal)
        return self.path

class Dijkstra(Pathfinder):
    def solve(self, start=(0,0), goal=(0,0)):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        visited = {}
        cost = {}
        visited[start] = None
        cost[start] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next in self.grid.neighbors(current):
                new_cost = cost[current] + self.grid.cost(next)
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    visited[next] = current

        self.path = self.reconstruct_path(visited, start, goal)
        return self.path

class Astar(Pathfinder):
    def solve(self, start=(0,0), goal=(0,0)):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        visited = {}
        cost = {}
        visited[start] = None
        cost[start] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next in self.grid.neighbors(current):
                new_cost = cost[current] + self.grid.cost(next)
                if next not in cost or new_cost < cost[next]:
                    cost[next] = new_cost
                    priority = new_cost + self.calculate_distance(goal, next)
                    frontier.put(next, priority)
                    visited[next] = current
                    
        self.path = self.reconstruct_path(visited, start, goal)        
        return self.path

        
            