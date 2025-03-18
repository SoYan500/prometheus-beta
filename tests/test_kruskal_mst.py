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
    
    # Verify that all vertices are connected in the MST
    vertex_set = set()
    for u, v, _ in mst:
        vertex_set.update([u, v])
    assert len(vertex_set) == 4
    
    # Verify the minimum possible total weight
    possible_min_weights = [
        ((2, 3, 4), (0, 3, 5), (0, 2, 6)),  # 15 total
        ((2, 3, 4), (0, 3, 5), (0, 1, 10))   # Alternate valid MST
    ]
    
    found_match = any(
        set(mst) == set(possible_mst) 
        for possible_mst in possible_min_weights
    )
    assert found_match, f"Unexpected MST edges: {mst}"

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