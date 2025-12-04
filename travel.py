import itertools

# Distance matrix: distance[i][j] is the distance from city i to city j
distance = [
    [0, 10, 15, 20],  # distances from city 0 to others
    [10, 0, 35, 25],  # city 1
    [15, 35, 0, 30],  # city 2
    [20, 25, 30, 0]   # city 3
]

# Number of cities
num_cities = len(distance)

# Generate all possible paths starting from city 0
cities = list(range(1, num_cities))  # excluding the starting city 0
min_path = None
min_cost = float('inf')

# Check all permutations of remaining cities
for perm in itertools.permutations(cities):
    path = [0] + list(perm) + [0]  # start and end at city 0
    cost = 0
    for i in range(len(path) - 1):
        cost += distance[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        min_path = path

# Output the result
print("Shortest path:", min_path)
print("Minimum cost:", min_cost)
