import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 220
    assert sorted(selected) == [1, 2]

def test_zero_capacity():
    """Test knapsack with zero capacity"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 0
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 0
    assert selected == []

def test_single_item():
    """Test knapsack with a single item"""
    weights = [10]
    values = [60]
    capacity = 5
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 0
    
    capacity = 10
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 60
    assert selected == [0]

def test_all_items_fit():
    """Test scenario where all items can fit in the knapsack"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 60
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 280
    assert sorted(selected) == [0, 1, 2]

def test_empty_input():
    """Test empty input lists"""
    weights = []
    values = []
    capacity = 50
    max_value, selected = solve_knapsack(weights, values, capacity)
    assert max_value == 0
    assert selected == []

def test_unequal_length_input():
    """Test input lists of different lengths"""
    weights = [10, 20]
    values = [60, 100, 120]
    capacity = 50
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack(weights, values, capacity)

def test_negative_capacity():
    """Test negative knapsack capacity"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = -10
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack(weights, values, capacity)