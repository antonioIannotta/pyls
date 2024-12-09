import pytest

from commands.ls_command import ls

def test_ls_with_visible_files():
    json_data = '{"contents": [{"name": "LICENSE"}, {"name": "README.md"}]}'
    assert ls(json_data) == "LICENSE README.md "

def test_ls_with_hidden_files():
    json_data = '{"contents": [{"name": ".gitignore"}, {"name": "token.go"}]}'
    assert ls(json_data) == "token.go "

def test_ls_with_mixed_files():
    json_data = '{"contents": [{"name": "token.go"}, {"name": ".gitignore"}, {"name": "go.mod"}]}'
    assert ls(json_data) == "token.go go.mod "

def test_ls_with_empty_contents():
    json_data = '{"contents": []}'
    assert ls(json_data) == ""

def test_ls_with_no_contents_key():
    json_data = '{}'
    with pytest.raises(KeyError):
        ls(json_data)