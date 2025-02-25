import pytest
from src.string_rotator import rotate_and_reverse

def test_basic_rotation_and_reverse():
    result = rotate_and_reverse("hello", 2)
    print(f"\nDiagnostic 'hello' rotated 2 times and reversed:")
    print(f"Rotated: {result}")
    print(f"Expected: lole")
    assert result == "lole"

def test_rotation_full_length():
    assert rotate_and_reverse("world", 5) == "dlrow"

def test_rotation_multiple_length():
    result = rotate_and_reverse("python", 8)
    print(f"\nDiagnostic 'python' rotated 8 times and reversed:")
    print(f"Rotated: {result}")
    print(f"Expected: nohtpy")
    assert result == "nohtpy"

def test_zero_rotations():
    assert rotate_and_reverse("test", 0) == "tset"

def test_empty_string():
    assert rotate_and_reverse("", 3) == ""

def test_invalid_string_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        rotate_and_reverse(123, 2)

def test_invalid_rotations_type():
    with pytest.raises(TypeError, match="Rotations must be an integer"):
        rotate_and_reverse("hello", "2")

def test_negative_rotations():
    with pytest.raises(ValueError, match="Rotations cannot be negative"):
        rotate_and_reverse("hello", -1)

def test_single_character():
    assert rotate_and_reverse("a", 3) == "a"

def test_long_string_rotation():
    result = rotate_and_reverse("abcdefg", 100)
    print(f"\nDiagnostic 'abcdefg' rotated 100 times and reversed:")
    print(f"Rotated: {result}")
    print(f"Expected: gfedcba")
    assert result == "gfedcba"