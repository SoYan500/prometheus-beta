import pytest
from src.string_utils import to_snake_case

def test_basic_conversion():
    """Test basic string conversions to snake_case"""
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("PascalCase") == "pascal_case"

def test_already_snake_case():
    """Test that already snake_case strings are not modified"""
    assert to_snake_case("hello_world") == "hello_world"
    assert to_snake_case("snake_case") == "snake_case"

def test_mixed_case_with_spaces():
    """Test conversion of strings with mixed case and spaces"""
    assert to_snake_case("Mixed Case String") == "mixed_case_string"
    assert to_snake_case("another Mixed Case") == "another_mixed_case"

def test_special_characters():
    """Test handling of special characters"""
    assert to_snake_case("Hello-World!") == "hello_world"
    assert to_snake_case("hello@world") == "hello_world"
    assert to_snake_case("hello world") == "hello_world"

def test_edge_cases():
    """Test edge cases like empty string, single word, etc."""
    assert to_snake_case("") == ""
    assert to_snake_case("SingleWord") == "single_word"
    assert to_snake_case("a") == "a"

def test_error_handling():
    """Test type error when input is not a string"""
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)

def test_numbers_and_mixed_cases():
    """Test conversion with numbers and mixed cases"""
    assert to_snake_case("hello2World") == "hello2_world"
    assert to_snake_case("Hello2World") == "hello2_world"
    assert to_snake_case("user123Name") == "user123_name"