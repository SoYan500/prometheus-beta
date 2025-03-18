from typing import List, Tuple, Dict

class DisjointSet:
    """
    A data structure to support union-find operations for Kruskal's algorithm.
    
    This class helps in efficiently determining if adding an edge would create a cycle
    by keeping track of connected components in the graph.
    """
    def __init__(self, vertices: int):
        """
        Initialize the disjoint set with each vertex in its own set.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root of a set with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Merge two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful (no cycle), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Kruskal's algorithm to find the Minimum Spanning Tree (MST).
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges, where each edge is (u, v, weight)
    
    Returns:
        List[Tuple[int, int, int]]: List of edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If the input is invalid
    """
    # Input validation
    if vertices < 0:
        raise ValueError("Number of vertices must be non-negative")
    
    if not edges:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize disjoint set
    disjoint_set = DisjointSet(vertices)
    
    # List to store MST edges
    mst_edges: List[Tuple[int, int, int]] = []
    
    # Process edges
    for edge in sorted_edges:
        u, v, weight = edge
        
        # Check if adding this edge creates a cycle
        if disjoint_set.union(u, v):
            # Use canonicalized order for sorted unpacking
            mst_edges.append(tuple(sorted((u, v)) + [weight]))
        
        # Stop when we have vertices-1 edges (complete MST)
        if len(mst_edges) == vertices - 1:
            break
    
    # Sort the final MST edges 
    return sorted(mst_edges, key=lambda x: x[2])