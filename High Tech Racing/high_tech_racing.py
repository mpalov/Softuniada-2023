import heapq


class Nodes:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


def store_path(graph, previous, paths):
    element = len(previous) - 1
    parent = previous[-1]
    while parent != -1:
        if parent in paths[element]:
            paths[element].remove(parent)
        else:
            paths[parent].add(element)
        element = parent
        parent = previous[parent]


def reverse_path(graph, previous):
    element = len(previous) - 1
    parent = previous[-1]
    while parent != -1:
        weight = graph[element][parent]
        del graph[element][parent]
        del graph[parent][element]

        graph[element][parent] = -weight
        element = parent
        parent = previous[parent]


def get_path(paths):
    start = 0
    end = len(paths) - 1
    path = []
    cur = start
    while cur != end:
        path.append(cur)
        next_ = paths[cur].pop()
        cur = next_
    path.append(end)
    return path


def dijkstra_alg(node, graph, potentials):
    previous = [-1] * len(node)

    for vertex in node:
        vertex.distance = float('inf')

    start = node[0]
    start.distance = 0
    priority_queue = [start]
    heapq.heapify(priority_queue)

    while priority_queue:
        current = heapq.heappop(priority_queue)
        for next_index, edge_weight in graph[current.index].items():
            next_n = node[next_index]
            new_distance = current.distance + edge_weight + potentials[current.index] - potentials[next_index]
            if new_distance < next_n.distance:
                next_n.distance = new_distance
                previous[next_n.index] = current.index
                heapq.heappush(priority_queue, next_n)
    return previous


nodes_count = int(input())

edge_count = int(input())
nodes = [Nodes(i, float('inf')) for i in range(nodes_count)]
graph = [{} for _ in range(nodes_count)]

paths = [set() for _ in range(nodes_count)]

for _ in range(edge_count):
    start, end, weight = [int(x) for x in input().split()]
    graph[start][end] = weight
    graph[end][start] = weight

candidates = [0] * nodes_count
prev = dijkstra_alg(nodes, graph, candidates)
store_path(graph, prev, paths)
reverse_path(graph, prev)

for i in range(len(candidates)):
    candidates[i] = nodes[i].distance

prev = dijkstra_alg(nodes, graph, candidates)
store_path(graph, prev, paths)
first_path = get_path(paths)

second_path = get_path(paths)

print(" -> ".join(map(str, first_path)))
print(" -> ".join(map(str, second_path)))
