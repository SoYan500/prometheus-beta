import pytest
from src.weekend_counter import count_weekends_in_month

def test_normal_months():
    # Test a few different months
    assert count_weekends_in_month(2023, 1) == 9  # January 2023
    assert count_weekends_in_month(2023, 6) == 8  # June 2023
    assert count_weekends_in_month(2023, 12) == 10  # December 2023

def test_leap_year():
    # Verify leap year works correctly
    assert count_weekends_in_month(2024, 2) == 8  # February 2024 (leap year)

def test_edge_cases():
    # Test first and last month of the year
    assert count_weekends_in_month(2023, 1) > 0  # January
    assert count_weekends_in_month(2023, 12) > 0  # December

def test_invalid_inputs():
    # Test invalid month inputs
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 0)
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 13)

def test_specific_month_patterns():
    # Some specific test cases for known month patterns
    assert count_weekends_in_month(2023, 2) == 8  # February 2023
    assert count_weekends_in_month(2023, 4) == 10  # April 2023
    assert count_weekends_in_month(2023, 5) == 10  # May 2023