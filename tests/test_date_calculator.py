import pytest
from datetime import date, timedelta
from src.date_calculator import calculate_days_between_dates

def test_same_date():
    """Test calculating days between the same date returns 0."""
    test_date = date(2023, 1, 1)
    assert calculate_days_between_dates(test_date, test_date) == 0

def test_different_dates():
    """Test calculating days between different dates."""
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_dates_in_reverse_order():
    """Test that order of dates doesn't matter."""
    date1 = date(2023, 1, 10)
    date2 = date(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 9

def test_date_strings():
    """Test calculating days using date strings."""
    assert calculate_days_between_dates("2023-01-01", "2023-01-10") == 9

def test_cross_year_dates():
    """Test calculating days across different years."""
    date1 = date(2022, 12, 31)
    date2 = date(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 1

def test_invalid_date_string_format():
    """Test raising ValueError for invalid date string format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("01-01-2023", "2023-01-10")

def test_invalid_input_type():
    """Test raising ValueError for invalid input types."""
    with pytest.raises(ValueError, match="Inputs must be date objects"):
        calculate_days_between_dates(123, "2023-01-10")

def test_long_time_span():
    """Test calculating days for dates far apart."""
    date1 = date(2000, 1, 1)
    date2 = date(2023, 1, 1)
    assert calculate_days_between_dates(date1, date2) == 8401  # Updated to match actual calculation