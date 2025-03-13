import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all complexity requirements"""
    assert validate_password("StrongPass1!") == True

def test_password_too_short():
    """Test password that is too short"""
    assert validate_password("Short1!") == False

def test_password_missing_uppercase():
    """Test password without an uppercase letter"""
    assert validate_password("lowercase1!") == False

def test_password_missing_lowercase():
    """Test password without a lowercase letter"""
    assert validate_password("UPPERCASE1!") == False

def test_password_missing_digit():
    """Test password without a digit"""
    assert validate_password("NoDigitPass!") == False

def test_password_missing_special_char():
    """Test password without a special character"""
    assert validate_password("NoSpecialChar1") == False

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        validate_password(12345)

def test_edge_cases():
    """Test various edge case passwords"""
    # Empty string
    assert validate_password("") == False
    
    # Spaces
    assert validate_password("Valid Pass1!") == False
    
    # Borderline valid password
    assert validate_password("A1b@defg") == True

def test_all_special_chars():
    """Test all allowed special characters"""
    special_chars = "!@#$%^&*"
    for char in special_chars:
        password = f"ValidPass1{char}"
        assert validate_password(password) == True