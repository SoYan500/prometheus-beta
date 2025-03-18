import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic DisjointSet operations."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union of vertices
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Repeated union should return False
    assert ds.union(0, 1) == False

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple graph."""
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Check MST edges
    assert len(mst) == 3
    
    # Check total weight
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 15
    
    # Verify MST properties
    assert set((edge[0], edge[1]) for edge in mst) == {(0, 3), (2, 3), (0, 2)}

def test_kruskal_mst_empty_graph():
    """Test MST for an empty graph."""
    assert kruskal_mst(0, []) == []

def test_kruskal_mst_single_vertex():
    """Test MST for a graph with a single vertex."""
    assert kruskal_mst(1, []) == []

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a graph with multiple components."""
    vertices = 6
    edges = [
        (0, 1, 1),
        (2, 3, 2),
        (4, 5, 3)
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    assert len(mst) == 3
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 6

def test_kruskal_mst_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [])

def test_kruskal_mst_total_weight():
    """Verify total weight of the MST."""
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Calculate total weight of MST
    total_weight = sum(edge[2] for edge in mst)
    
    assert total_weight == 15  # 4 + 5 + 6