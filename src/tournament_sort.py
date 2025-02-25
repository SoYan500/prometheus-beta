from typing import List, TypeVar, Callable

T = TypeVar('T')

def tournament_sort(arr: List[T], compare: Callable[[T, T], bool] = lambda x, y: x < y) -> List[T]:
    """
    Implement the tournament sort algorithm.
    
    Tournament sort is a sorting algorithm that uses a tournament tree (binary heap)
    to sort elements efficiently.
    
    Args:
        arr (List[T]): The input list to be sorted
        compare (Callable[[T, T], bool], optional): Comparison function. 
            Defaults to less than comparison for ascending order.
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Cannot sort an empty list")
    
    # Handle single element list
    if len(arr) == 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    elements = arr.copy()
    
    # Create tournament tree
    def create_tournament_tree(elements):
        # If odd number of elements, add a sentinel
        if len(elements) % 2 != 0:
            elements.append(elements[-1])
        
        # Initialize tournament tree
        tree = elements.copy()
        
        # Build the tournament tree from bottom up
        n = len(elements)
        while n > 1:
            for i in range(0, n, 2):
                # Compare adjacent pairs
                if i + 1 < n:
                    winner_index = i if compare(elements[i], elements[i+1]) else i+1
                    # Replace the pair with the winner
                    tree[i // 2] = elements[winner_index]
            
            # Reduce tree size by half and update elements
            n //= 2
            elements = tree[:n]
        
        return tree[0]
    
    # Sorted list to return
    sorted_list = []
    
    # Continue until all elements are sorted
    while len(elements) > 0:
        # Find the current tournament winner
        winner = create_tournament_tree(elements)
        sorted_list.append(winner)
        
        # Remove the winner from the list
        elements.remove(winner)
    
    return sorted_list