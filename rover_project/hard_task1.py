from collections import deque

# Step 1: Read file
def read_obstacles(filename):
    obstacles = []
    with open(filename, 'r') as f:
        for line in f:
            n, e, s, w = map(int, line.split())
            x = e - w
            y = n - s
            obstacles.append((x, y))
    return obstacles

# Step 2: Create grid
def create_grid(size, obstacles):
    grid = [[1 for _ in range(size)] for _ in range(size)]

    for x, y in obstacles:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = 0   # mark obstacle

    return grid

# Step 3: Print grid
def print_grid(grid):
    for row in grid:
        print(row)

# Step 4: BFS shortest path
def shortest_path(grid, start, end):
    size = len(grid)
    queue = deque()
    queue.append((start[0], start[1], 0))  # (x, y, distance)

    visited = set()
    visited.add(start)

    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # N,S,E,W

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < size and 0 <= ny < size and
                grid[ny][nx] == 1 and (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1  # no path


# ---- MAIN ----
size = 11
obstacles = read_obstacles("sample.txt")

grid = create_grid(size, obstacles)

print("Arena Map:")
print_grid(grid)

start = (0, 0)
end = (10, 10)

distance = shortest_path(grid, start, end)

print("\nShortest Path Distance:", distance)