import pytest
from src.parenthesis_validator import is_nested_parentheses

def test_simple_nested_parentheses():
    assert is_nested_parentheses("()") == True

def test_complex_nested_parentheses():
    assert is_nested_parentheses("(())") == True
    assert is_nested_parentheses("((()))") == True

def test_incorrect_order_parentheses():
    assert is_nested_parentheses(")(") == False

def test_unbalanced_parentheses():
    assert is_nested_parentheses("((()") == False
    assert is_nested_parentheses("())") == False

def test_empty_string():
    assert is_nested_parentheses("") == True

def test_nested_with_other_characters():
    assert is_nested_parentheses("a(b)c") == True
    assert is_nested_parentheses("(a(b)c)") == True

def test_multiple_sets_of_parentheses():
    assert is_nested_parentheses("()(())()") == True
    assert is_nested_parentheses("(()())") == True

def test_only_opening_or_closing_parentheses():
    assert is_nested_parentheses("(((") == False
    assert is_nested_parentheses(")))") == False

@pytest.mark.parametrize("input_str", [
    "()",
    "(())",
    "((()))",
    "",
    "a(b)c",
    "(a(b)c)",
    "()(())())",
])
def test_valid_inputs(input_str):
    assert is_nested_parentheses(input_str) is not None