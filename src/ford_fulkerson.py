from typing import List, Dict, Optional
from collections import deque

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           adjacent nodes and their edge capacities.
        source (str): The source node of the flow network.
        sink (str): The sink node of the flow network.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input strictly
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in graph")
    
    # Create a deep copy of the graph
    graph_copy = {node: dict(edges) for node, edges in graph.items()}
    
    # Ensure all nodes exist in the graph
    all_nodes = set(graph_copy.keys()) | set(node for edges in graph_copy.values() for node in edges)
    for node in all_nodes:
        if node not in graph_copy:
            graph_copy[node] = {}
    
    # Create a residual graph
    def create_residual_graph(graph):
        residual = {}
        for node in graph:
            residual[node] = {}
            for neighbor, capacity in graph[node].items():
                # Forward edge
                residual[node].setdefault(neighbor, 0)
                residual[node][neighbor] += capacity
                # Backward edge (for flow adjustment)
                if neighbor not in residual:
                    residual[neighbor] = {}
                residual[neighbor].setdefault(node, 0)
        return residual
    
    # Breadth-first search to find augmenting path
    def bfs(residual, source, sink, parent):
        # Reset parent mapping
        for node in parent:
            parent[node] = None
        
        # Track visited nodes
        visited = set()
        
        # Queue for BFS
        queue = deque([source])
        visited.add(source)
        parent[source] = source
        
        while queue:
            current = queue.popleft()
            
            # Check all neighbors
            for neighbor, capacity in residual[current].items():
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    # Path found to sink
                    if neighbor == sink:
                        return True
        
        return False
    
    # Create residual graph
    residual = create_residual_graph(graph_copy)
    
    # Initialize parent mapping and max flow
    nodes = list(residual.keys())
    parent = {node: None for node in nodes}
    max_flow = 0
    
    # Find augmenting paths
    while bfs(residual, source, sink, parent):
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual[prev][current])
            current = prev
        
        # Update residual capacities
        current = sink
        while current != source:
            prev = parent[current]
            residual[prev][current] -= path_flow
            residual[current].setdefault(prev, 0)
            residual[current][prev] += path_flow
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow