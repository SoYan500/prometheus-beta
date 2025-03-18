"""
Test suite for file extension extraction function.
"""
import pytest
from src.file_extension import get_file_extension


def test_get_file_extension_with_normal_filename():
    """Test extracting extension from a typical filename."""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.JPEG') == 'jpeg'
    assert get_file_extension('script.py') == 'py'


def test_get_file_extension_with_full_path():
    """Test extracting extension from full file paths."""
    assert get_file_extension('/home/user/document.pdf') == 'pdf'
    assert get_file_extension('C:\\Users\\name\\file.docx') == 'docx'


def test_get_file_extension_with_no_extension():
    """Test behavior with files having no extension."""
    assert get_file_extension('README') == ''
    assert get_file_extension('/path/to/file_without_ext') == ''


def test_get_file_extension_with_multiple_dots():
    """Test behavior with filenames containing multiple dots."""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('document.backup.txt') == 'txt'


def test_get_file_extension_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        get_file_extension(123)
    with pytest.raises(TypeError):
        get_file_extension(None)
    with pytest.raises(TypeError):
        get_file_extension(['file.txt'])