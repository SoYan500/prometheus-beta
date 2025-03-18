import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_initialization():
    """Test DisjointSet initialization"""
    ds = DisjointSet(5)
    assert ds.parent == [0, 1, 2, 3, 4]
    assert ds.rank == [0, 0, 0, 0, 0]

def test_disjoint_set_find():
    """Test find method of DisjointSet"""
    ds = DisjointSet(5)
    for i in range(5):
        assert ds.find(i) == i

def test_disjoint_set_union():
    """Test union method of DisjointSet"""
    ds = DisjointSet(5)
    
    # First union
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Repeated union should return False
    assert ds.union(0, 1) == False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph with 4 vertices: [(weight, u, v), ...]
    graph = [
        (1, 0, 1),  # Edge between vertex 0 and 1 with weight 1
        (4, 1, 2),  # Edge between vertex 1 and 2 with weight 4
        (2, 2, 3),  # Edge between vertex 2 and 3 with weight 2
        (3, 0, 3),  # Edge between vertex 0 and 3 with weight 3
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have n-1 edges (for n vertices)
    assert len(mst) == 3
    
    # Check total weight of MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph"""
    graph = [
        (1, 0, 1),
        (4, 1, 2),
        (10, 3, 4),
    ]
    
    mst = kruskal_mst(graph)
    
    # Should still create a spanning tree
    assert len(mst) == 2

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty graph"""
    with pytest.raises(ValueError):
        kruskal_mst([])

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with single vertex"""
    graph = [(1, 0, 0)]
    mst = kruskal_mst(graph)
    assert len(mst) == 0  # No edges in minimal spanning tree