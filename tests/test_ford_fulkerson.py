import pytest
from src.ford_fulkerson import ford_fulkerson

def test_basic_flow():
    """Test a simple flow network with a clear maximum flow."""
    graph = {
        's': {'a': 10, 'c': 10},
        'a': {'b': 4, 'c': 2, 'd': 8},
        'b': {'t': 10},
        'c': {'d': 9},
        'd': {'b': 6, 't': 10},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 19

def test_no_flow_possible():
    """Test a graph where no flow is possible."""
    graph = {
        's': {},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 0

def test_complex_flow_network():
    """Test a more complex flow network."""
    graph = {
        's': {'a': 3, 'c': 3},
        'a': {'b': 4},
        'b': {'t': 5},
        'c': {'d': 6},
        'd': {'t': 5}
    }
    assert ford_fulkerson(graph, 's', 't') == 6

def test_single_path_flow():
    """Test a flow network with only one possible path."""
    graph = {
        's': {'a': 10},
        'a': {'t': 10}
    }
    assert ford_fulkerson(graph, 's', 't') == 10

def test_multiple_paths_flow():
    """Test a flow network with multiple possible paths."""
    graph = {
        's': {'a': 10, 'b': 10},
        'a': {'t': 5},
        'b': {'t': 10}
    }
    assert ford_fulkerson(graph, 's', 't') == 15

def test_invalid_source_node():
    """Test handling of invalid source node."""
    graph = {
        'a': {'b': 10},
        'b': {'c': 10}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in graph"):
        ford_fulkerson(graph, 's', 'b')

def test_invalid_sink_node():
    """Test handling of invalid sink node."""
    graph = {
        's': {'a': 10},
        'a': {'b': 10}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in graph"):
        ford_fulkerson(graph, 's', 't')

def test_bidirectional_flow():
    """Test a graph with potential bidirectional flow."""
    graph = {
        's': {'a': 10, 'b': 10},
        'a': {'b': 2, 't': 5},
        'b': {'a': 1, 't': 15}
    }
    assert ford_fulkerson(graph, 's', 't') == 20