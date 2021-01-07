import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float("inf") for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # since nodes can be added to the heap multiple times, we only process
        # a vertex the fist time we remove it from the heap.
        if current_distance > distances[current_vertex]:
            continue

        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # only consider this new path if dist < any current path
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances


example_graph = {
    "U": {"V": 2, "W": 5, "X": 1},
    "V": {"U": 2, "X": 2, "W": 3},
    "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
    "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
    "Y": {"X": 1, "W": 1, "Z": 1},
    "Z": {"W": 5, "Y": 1},
}
print(calculate_distances(example_graph, "X"))
