import pytest
from challenges.breadth_first.breadth_first import BreadthFirstGraph


def test_one_vertex(bfg):
    """
    Walk of graph with one vertex see one vertex.
    """

    node = bfg.add_node('cat')

    expected = [node]
    actual = bfg.breadth_first(node)
    assert actual == expected


def test_directed_graph():
    """
    From starting node walk directed graph in breadth first order and see list of seen nodes in order.
    """
    pass


def test_cyclic_graph():
    """
    From starting node walk cyclic graph in breadth first order and see list of seens nodes in order.
    """
    pass


def test_island():
    """
    Only see connected verices in walk of graph.
    """
    pass


# Fixtures


@pytest.fixture
def bfg():
    """
    Instance of BreadthFirstGraph
    """

    return BreadthFirstGraph()
