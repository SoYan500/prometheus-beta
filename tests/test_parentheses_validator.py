import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_empty_string():
    """Test that an empty string is considered balanced."""
    assert is_balanced_parentheses("") == True

def test_simple_balanced_parentheses():
    """Test simple balanced parentheses."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("((()))") == True

def test_nested_balanced_parentheses():
    """Test nested balanced parentheses."""
    assert is_balanced_parentheses("(())()") == True
    assert is_balanced_parentheses("((()()))") == True

def test_unbalanced_parentheses():
    """Test unbalanced parentheses scenarios."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False

def test_invalid_input():
    """Test that invalid input raises a ValueError."""
    with pytest.raises(ValueError):
        is_balanced_parentheses("(a)")
    with pytest.raises(ValueError):
        is_balanced_parentheses("hello")
    with pytest.raises(ValueError):
        is_balanced_parentheses("(123)")