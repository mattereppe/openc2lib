import pytest
import random
import string
from openc2lib import File, Hashes, Binaryx
from openc2lib.types.base import ArrayOf, Array

# Function to generate random strings
def random_strings():
    rnd = []
    for length in range(10, 15):
        rnd.append(''.join(random.choices(string.ascii_lowercase, k=length)))
        rnd.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=length)))
        rnd.append(''.join(random.choices(string.printable, k=length)))
    return rnd

# Example hashes for testing
hashes = {'md5': Binaryx("AABBCCDDEEFF00112233445566778899"), 'sha1': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDD"), 'sha256': Binaryx("AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899")}

# Test random file creation inside ArrayOf
@pytest.mark.parametrize("name", random_strings())
@pytest.mark.parametrize("path", random_strings())
def test_array_of_files(name, path):
    # Create a list of File objects
    files = [File({'name': name, 'path': path}) for _ in range(5)]  # Create 5 File objects
    array_of_files = ArrayOf(File)(files)  # Wrap them in ArrayOf
    
    assert isinstance(array_of_files, Array)  # Assert it's an ArrayOf
    assert all(isinstance(f, File) for f in array_of_files)  # Ensure all items are File instances

# Test static parameters for files inside ArrayOf
@pytest.mark.parametrize("name", ["test.txt"])
@pytest.mark.parametrize("path", ["/var/run/myprocess"])
def test_static_array_of_files(name, path):
    # Create a list of File objects
    files = [File({'name': name, 'path': path}) for _ in range(3)]  # Create 3 File objects
    array_of_files = ArrayOf(File)(files)  # Wrap them in ArrayOf
    
    assert isinstance(array_of_files, Array)  # Assert it's an ArrayOf
    assert len(array_of_files) == 3  # Assert the length is 3
    assert all(isinstance(f, File) for f in array_of_files)  # Ensure all items are File instances

# Test ArrayOf with hashes added to files
@pytest.mark.parametrize("name", random_strings())
@pytest.mark.parametrize("path", random_strings())
@pytest.mark.parametrize("hashes", [hashes])  # Example hashes
def test_array_of_files_with_hashes(name, path, hashes):
    # Create files with hashes
    files = [
        File({'name': name, 'path': path, 'hashes': Hashes(hashes)})
        for _ in range(3)
    ]
    array_of_files = ArrayOf(File)(files)  # Wrap them in ArrayOf
    
    assert isinstance(array_of_files, Array)  # Assert it's an ArrayOf
    assert len(array_of_files) == 3  # Assert the length is 3
    assert all(isinstance(f, File) for f in array_of_files)  # Ensure all items are File instances
    assert all('hashes' in f for f in array_of_files)  # Verify that each file has hashes

# Test invalid ArrayOf (too many files)
def test_array_of_files_exceeding_maximum():
    # Create 11 files (assuming max is 10)
    files = [File({'name': 'file', 'path': '/var/run/file', 'hashes': Hashes(hashes)}) for _ in range(11)]
    
    with pytest.raises(ValueError):  # Assuming validation will raise an error for exceeding max
        array_of_files = ArrayOf(File)(files)
        array_of_files.validate(types=True, num_max=10)  # This should raise an error due to too many items

# Test invalid ArrayOf (missing file)
def test_array_of_files_missing_file():
    with pytest.raises(TypeError):  # Assuming TypeError if not all items are of type File
        array_of_files = ArrayOf(File, [None, File({'name': 'file', 'path': '/var/run/file'})])


