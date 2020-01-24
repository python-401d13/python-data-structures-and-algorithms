import pytest
from graph import Graph, Vertex


def test_add_node(graph):
    """
    Add a vertex to a graph.
    """

    value = 'apple'

    expected = Vertex(value).value
    vertex = graph.add_node(value)

    assert isinstance(vertex, Vertex)
    assert vertex.value == expected


def test_add_edge_no_start_vertex(graph):
    """
    Fail to add edge from vertex not in graph.
    """

    graph.add_node('apple')
    banana = graph.add_node('banana')
    carrot = Vertex('carrot')

    with pytest.raises(KeyError):
        graph.add_edge(carrot, banana)


def test_add_edge_no_end_vertex(graph):
    """
    Fail to add edge to vertex not in graph.
    """

    apple = graph.add_node('apple')
    graph.add_node('banana')
    carrot = Vertex('carrot')

    with pytest.raises(KeyError):
        graph.add_edge(apple, carrot)


def test_add_edge(graph):
    """
    Add directed edge between two vertices in graph.
    """

    apple = graph.add_node('apple')
    banana = graph.add_node('banana')

    graph.add_edge(apple, banana)

    expected = (banana, 0)
    actual = graph._adjacency_list[apple][0]

    assert actual == expected


def test_add_edge_with_weight(graph):
    """
    Add directed edge between two vertices in graph with weight.
    """

    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    weight = 102

    graph.add_edge(apple, banana, weight)

    expected = (banana, weight)
    actual = graph._adjacency_list[apple][0]

    assert actual == expected


def test_get_nodes_empty(graph):
    """
    Get an empty collection of vertices when a graph has no vertices.
    """

    expected = set({})
    actual = set(graph.get_nodes())

    assert actual == expected


def test_get_nodes(graph):
    """
    Get a collection of al vertices in a graph.
    """

    apple = graph.add_node('apple')
    banana = graph.add_node('banana')
    carrot = graph.add_node('carrot')

    expected = set({apple, banana, carrot})
    actual = set(graph.get_nodes())

    assert actual == expected


def test_get_nodes_no_neighbors(graph):
    """
    A graph vertex with no neighbors is shown as an empty collection.
    """

    apple = graph.add_node('apple')

    expected = []
    actual = graph.get_neighbors(apple)

    assert actual == expected


def test_get_neighbors(graph):
    """
    Neighbors of a graph vertex are gotten.
    """

    apple = graph.add_node('apple')
    banana = graph.add_node('banana')

    graph.add_edge(apple, banana)

    expected = [(banana, 0)]
    actual = graph.get_neighbors(apple)

    assert actual == expected


def test_size_empty(graph):
    """
    See size of empty graph.
    """

    expected = 0
    actual = graph.size()

    assert actual == expected


def test_size(graph):
    """
    See size of non-empty graph.
    """

    graph.add_node('apple')

    expected = 1
    actual = graph.size()

    assert actual == expected


# Fixtures


@pytest.fixture
def graph():
    """
    Create Graph instance.
    """

    return Graph()
