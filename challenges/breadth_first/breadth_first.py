from challenges.graph.graph import Graph
from challenges.stacks_and_queues.stacks_and_queues import Queue

class BreadthFirstGraph(Graph):
    """
    Extention of Graph class with breadth first traversal method.
    """

    def __init__(self):
        """
        BreadthFirstGraph constructor.
        """

        super().__init__()


    def breadth_first(self, vertex):
        """
        Traverse a graph in breadth first order given a starting vertex,
        return a collection of all vertices visited in the order they were visited.

        In:
        vertex (Vertex): The starting vertex.

        Out:
        (list): Collection of vertices visisted in the order they were visited.
        """

        vertices = []
        queue = Queue()

        queue.enqueue(vertex)

        while not queue.is_empty():
            queue_vertex = queue.dequeue()

            if queue_vertex in vertices:
                continue

            for neighbor in self.get_neighbors(queue_vertex):
                queue.enqueue(neighbor)

            vertices.append(queue_vertex)

        return vertices
