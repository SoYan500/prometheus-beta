import os
import pytest
from cryptography.fernet import Fernet
import src.file_decryption as file_decryption

@pytest.fixture
def setup_encrypted_file(tmp_path):
    """Create a temporary encrypted file for testing."""
    # Generate a key
    key = Fernet.generate_key()
    key_path = tmp_path / "test_key.key"
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    # Create original file
    original_content = b"This is a secret message!"
    original_file_path = tmp_path / "original.txt"
    with open(original_file_path, 'wb') as f:
        f.write(original_content)

    # Encrypt the file
    fernet = Fernet(key)
    encrypted_content = fernet.encrypt(original_content)
    encrypted_file_path = tmp_path / "encrypted.txt"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)

    return {
        'key_path': str(key_path),
        'encrypted_file_path': str(encrypted_file_path),
        'original_content': original_content
    }

def test_successful_decryption(setup_encrypted_file, tmp_path):
    """Test successful file decryption."""
    decrypted_path = file_decryption.decrypt_file(
        setup_encrypted_file['encrypted_file_path'], 
        setup_encrypted_file['key_path']
    )
    
    # Verify decrypted file exists
    assert os.path.exists(decrypted_path)
    
    # Verify content
    with open(decrypted_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == setup_encrypted_file['original_content']

def test_custom_output_path(setup_encrypted_file, tmp_path):
    """Test decryption with a custom output path."""
    custom_output = str(tmp_path / "custom_decrypted.txt")
    decrypted_path = file_decryption.decrypt_file(
        setup_encrypted_file['encrypted_file_path'], 
        setup_encrypted_file['key_path'], 
        output_path=custom_output
    )
    
    assert decrypted_path == custom_output
    
    with open(decrypted_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == setup_encrypted_file['original_content']

def test_nonexistent_encrypted_file(tmp_path):
    """Test handling of nonexistent encrypted file."""
    nonexistent_file = str(tmp_path / "nonexistent.txt")
    key_path = str(tmp_path / "key.key")
    
    with open(key_path, 'wb') as f:
        f.write(Fernet.generate_key())
    
    with pytest.raises(FileNotFoundError):
        file_decryption.decrypt_file(nonexistent_file, key_path)

def test_nonexistent_key_file(setup_encrypted_file, tmp_path):
    """Test handling of nonexistent key file."""
    nonexistent_key = str(tmp_path / "nonexistent_key.key")
    
    with pytest.raises(FileNotFoundError):
        file_decryption.decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            nonexistent_key
        )

def test_invalid_key(setup_encrypted_file, tmp_path):
    """Test handling of invalid decryption key."""
    invalid_key_path = str(tmp_path / "invalid_key.key")
    with open(invalid_key_path, 'wb') as f:
        f.write(b'invalid_key_data')
    
    with pytest.raises(ValueError):
        file_decryption.decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            invalid_key_path
        )