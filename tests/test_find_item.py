import pytest
from utils import find_item

# Sample directory structure for tests
directory_structure = [
    {"name": "README.md", "type": "file"},
    {"name": "interpreter", "type": "directory", "contents": [
        {"name": "LICENSE", "type": "file"},
        {"name": "parser", "type": "directory", "contents": [
            {"name": "parser.go", "type": "file"}
        ]}
    ]},
    {"name": "token", "type": "directory", "contents": [
        {"name": "token.go", "type": "file"}
    ]}
]

def test_find_item_file_in_root():
    result = find_item(directory_structure, "README.md")
    assert result == {"name": "README.md", "type": "file"}

def test_find_item_file_in_nested_folder():
    result = find_item(directory_structure, "parser.go")
    assert result == {"name": "parser.go", "type": "file"}

def test_find_item_folder_in_root():
    result = find_item(directory_structure, "interpreter")
    assert result == {"name": "interpreter", "type": "directory", "contents": [
        {"name": "LICENSE", "type": "file"},
        {"name": "parser", "type": "directory", "contents": [
            {"name": "parser.go", "type": "file"}
        ]}
    ]}

def test_find_item_file_with_path():
    result = find_item(directory_structure, "./interpreter/LICENSE")
    assert result == {"name": "LICENSE", "type": "file"}

def test_find_item_file_with_subfolder_path():
    result = find_item(directory_structure, "./interpreter/parser/parser.go")
    assert result == {"name": "parser.go", "type": "file"}

def test_find_item_non_existent_file():
    result = find_item(directory_structure, "None")
    assert result is None

def test_find_item_empty_contents():
    result = find_item([], "README.md")
    assert result is None

def test_find_item_invalid_path():
    result = find_item(directory_structure, "/invalid/path/file.txt")
    assert result is None