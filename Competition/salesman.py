import heapq

def shortest_distances(n, m, edges, s):
    # Create an adjacency list to represent the graph
    graph = {}
    for x, y, r in edges:
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append((y, r))
        graph[y].append((x, r))

    # Initialize distances to all cities as infinity
    distances = {city: float('inf') for city in range(1, n+1)}
    distances[s] = 0

    # Create a priority queue (min-heap) for Dijkstra's algorithm
    queue = [(0, s)]

    while queue:
        dist, current_city = heapq.heappop(queue)

        if dist > distances[current_city]:
            continue

        for neighbor, weight in graph.get(current_city, []):
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    return distances

def dijkstra(graph, start):
    distances = {city: float('infinity') for city in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_distance > distances[current_city]:
            continue

        for adjacent, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

def create_graph(num_cities, num_roads, roads, start_city):
    # Initialize an empty graph
    graph = {city: {} for city in range(1, num_cities + 1)}

    # Add the roads to the graph
    for road in roads:
        start, destination, length = road
        graph[start][destination] = length
        graph[destination][start] = length  # The roads are bidirectional

    return graph

test_cases = int(input())

for _ in range(test_cases):
    first_line = input().split()
    n,m = int(first_line[0]), int(first_line[1])  # Number of cities and roads

    next_m_lines = [input().split() for _ in range(m)]
    # convert to int
    edges = []
    for x, y, r in next_m_lines:
        edges.append((int(x), int(y), int(r)))
    s = int(input())  # Starting location of the salesman

    graph = create_graph(n, m, edges, s)
    #print(graph)
    distances = shortest_distances(n, m, edges, s)
    distances2 = dijkstra(graph, s)
    # print distances. skip 0. print -1 if infinity
    for i in range(1, n+1):
        if i != s:
            print(distances2[i] if distances[i] != float('inf') else -1, end=' ')