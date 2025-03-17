import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test freezing point conversion."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test boiling point conversion."""
    assert fahrenheit_to_celsius(212) == 100

def test_negative_temperature():
    """Test negative temperature conversion."""
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_temperature():
    """Test decimal temperature conversion."""
    assert fahrenheit_to_celsius(98.6) == 37

def test_large_number():
    """Test large temperature number."""
    assert fahrenheit_to_celsius(1000) == 537.78

def test_invalid_input_type():
    """Test that non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")

def test_input_float():
    """Test conversion with float input."""
    assert fahrenheit_to_celsius(68.5) == 20.28