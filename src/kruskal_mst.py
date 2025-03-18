class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help implement Kruskal's algorithm.
    
    This class provides efficient methods for finding the set of an element
    and merging sets during Minimum Spanning Tree construction.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set data structure.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root (representative) of a set with path compression.
        
        :param item: The vertex to find the set for
        :return: The root of the set containing the vertex
        """
        if self.parent[item] != item:
            # Path compression: make every node on the path point to the root
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Merge two sets using union by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if sets were merged, False if already in same set
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If roots are same, vertices are in same set
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are same, make one as root and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's algorithm.
    
    :param graph: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    :raises ValueError: If graph is empty or None
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(graph)
    
    # Find number of vertices
    vertices = max(max(u, v) for _, u, v in graph) + 1
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Process edges in sorted order
    for weight, u, v in sorted_edges:
        # If including this edge doesn't form a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
    
    return mst