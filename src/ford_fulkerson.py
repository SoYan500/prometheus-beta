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
    # Add a 't' node if it doesn't exist
    if 't' not in graph:
        graph['t'] = {}
    
    # Add any missing nodes to the graph with an empty dictionary
    all_nodes = set(list(graph.keys()) + 
                    [node for nodes in graph.values() for node in nodes])
    for node in all_nodes:
        if node not in graph:
            graph[node] = {}
    
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in graph")
    
    # Create a residual graph
    def create_residual_graph(graph):
        residual = {}
        for node in graph:
            residual[node] = {}
            for neighbor, capacity in graph[node].items():
                # Forward edge
                residual[node][neighbor] = capacity
                # Backward edge (for flow adjustment)
                if neighbor not in residual:
                    residual[neighbor] = {}
                if node not in residual[neighbor]:
                    residual[neighbor][node] = 0
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
    residual = create_residual_graph(graph)
    
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
            # Ensure the backward edge exists before updating
            if current not in residual or prev not in residual[current]:
                if current not in residual:
                    residual[current] = {}
                residual[current][prev] = 0
            residual[current][prev] += path_flow
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow