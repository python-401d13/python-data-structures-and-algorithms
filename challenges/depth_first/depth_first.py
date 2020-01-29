
def depth_first(graph, vertex):
    """
    Walk a graph in depth first pre-order.

    In:
    graph (Graph): The graph to walk.
    vertex (Vertex): The vertex to start walking from.

    Out:
    vertices (set): A set of the vertices walked in depth first pre-order.
    """

    vertices = set({})

    graph_vertices = graph.get_nodes()

    if not graph_vertices:
        return vertices

    if vertex not in graph_vertices:
        return vertices

    def walk(graph, vertex, vertices):
        """
        Walk graph.
        """

        if vertex in vertices:
            return

        vertices.add(vertex)

        neighbors = graph.get_neighbors(vertex)
        for neighbor in neighbors:
            walk(graph, neighbor[0], vertices)

    walk(graph, vertex, vertices)

    return vertices
