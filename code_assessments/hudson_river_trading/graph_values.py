import pytest


class Vertex:
    def __init__(self, id):
        self.id = id
        self.val = None
        self.conn = []  # List of connected vertices

    def __lt__(self, vertex_compare):
        # Sorting built-in
        return len(self.conn) < len(vertex_compare.conn)

def solution(N, A, B):
    # create unique vertices
    map_a, map_b = {}, {}
    for id in A:
        if id not in map_a.keys():
            new_vertex = Vertex(id=id)
            map_a[id] = new_vertex
    for id in B:
        if id not in map_b.keys():
            if id not in map_a.keys():
                vertex = Vertex(id=id)
            else:
                vertex = map_a[id]
            map_b[id] = vertex

    # Link vertices
    for i in range(len(A)):
        id_a, id_b = A[i], B[i]
        map_a[id_a].conn.append(map_b[id_b])
        map_b[id_b].conn.append(map_a[id_a])

    # Get rid of values 1:N that won't be used, due to unconnected vertices
    values = list(range(1, N + 1))
    for id in values:
        # If a vertex has no connections after the graph is built, then pop min value
        # from values.
        if id not in map_a.keys() and id not in map_b.keys():
            values.pop(0)

    # Get a list of all vertices
    vertices_all = []
    for vertex in map_a.values():
        if vertex not in vertices_all:
            vertices_all.append(vertex)
    for vertex in map_b.values():
        if vertex not in vertices_all:
            vertices_all.append(vertex)

    # Sort by connections in descending order
    vertices_all.sort()
    vertices_all = vertices_all[::-1]

    # Traverse the graph, and give the largest value to the vertices with the most connections
    # Find the vertex with the most connections, that has no value assigned, and give it the max value
    for i in range(len(vertices_all)):
        max_vertex = vertices_all[i]
        max_vertex.val = values.pop()

    # Traverse the graph, and calculate edges
    map_edges = {}
    total = 0
    for vertex in vertices_all:
        for conn in vertex.conn:
            value_edge = vertex.val + conn.val
            total += value_edge
            map_edges[value_edge] = 0
    total /= 2
    return total


test_cases = [(5, [2, 2, 1, 2], [1, 3, 4, 4], 31),
              (3, [1], [3], 5),
              (4, [1, 3], [2, 4], 10)]

@pytest.mark.parametrize("N, A, B, expected", test_cases)
def test_vertex_values(N, A, B, expected):
    total = solution(N=N, A=A, B=B)
    assert total == expected
