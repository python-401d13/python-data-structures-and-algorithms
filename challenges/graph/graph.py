
class Graph():
    """
    Common graph data structure.
    """

    def __init__(self):
        """
        Graph constructor.
        """

        self._adjacency_list = {}


    def add_node(self, value):
        """
        Add a vertex to a graph.

        In:
        value (): New vertex value.

        Out:
        (Vertex): New vertex added to graph.
        """

        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex


    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Add an edge between two nodes in a graph.

        In:
        start_vertex (Vertex): Node to add directed edge from.
        end_vertex (Vertex): Node to add directed edge to.
        weight (int): Cost of directed edge.
        """

        if start_vertex not in self._adjacency_list:
            raise KeyError('No start vertex.')

        if end_vertex not in self._adjacency_list:
            raise KeyError('No end vertex.')

        self._adjacency_list[start_vertex].append((end_vertex, weight))


    def get_nodes(self):
        """
        Get collection of all vertices in graph.

        Out:
        (list): Collection of all vertices in graph.
        """

        return self._adjacency_list.keys()


    def get_neighbors(self, start_vertex):
        """
        Get collection of neighbors for a vertex in graph.

        In:
        start_vertex (Vertex): Get neighbors of the vertex.

        Out:
        (list): Neighbors of the vertex.
        """

        return self._adjacency_list[start_vertex]


    def size(self):
        """
        See the number of vertices in a graph.
        """

        return len(self._adjacency_list)


class Vertex():
    """
    Node to common graph data structure.
    """

    def __init__(self, value):
        """
        Vertex constructor.
        """

        self.value = value
