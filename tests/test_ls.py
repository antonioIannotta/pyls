import pytest
import json

from commands.ls_command import ls

# Sample JSON data for testing
TEST_JSON_DATA = {
    "name": "interpreter",
    "size": 4096,
    "time_modified": 1699957865,
    "permissions": "-rw-r--r--",
    "contents": [
        {
            "name": ".gitignore",
            "size": 8911,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "LICENSE",
            "size": 1071,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "README.md",
            "size": 83,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "ast",
            "size": 4096,
            "time_modified": 1699957739,
            "permissions": "-rw-r--r--",
            "contents": [
                {
                    "name": "go.mod",
                    "size": 225,
                    "time_modified": 1699957780,
                    "permissions": "-rw-r--r--"
                },
                {
                    "name": "ast.go",
                    "size": 837,
                    "time_modified": 1699957719,
                    "permissions": "drwxr-xr-x"
                }
            ]
        },
        {
            "name": "go.mod",
            "size": 60,
            "time_modified": 1699950073,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "lexer",
            "size": 4096,
            "time_modified": 1699955487,
            "permissions": "drwxr-xr-x",
            "contents": [
                {
                    "name": "lexer_test.go",
                    "size": 1729,
                    "time_modified": 1699955126,
                    "permissions": "drwxr-xr-x"
                },
                {
                    "name": "go.mod",
                    "size": 227,
                    "time_modified": 1699944819,
                    "permissions": "-rw-r--r--"
                },
                {
                    "name": "lexer.go",
                    "size": 2886,
                    "time_modified": 1699955487,
                    "permissions": "drwxr-xr-x"
                }
            ]
        },
        {
            "name": "main.go",
            "size": 74,
            "time_modified": 1699950453,
            "permissions": "-rw-r--r--"
        },
        {
            "name": "parser",
            "size": 4096,
            "time_modified": 1700205662,
            "permissions": "drwxr-xr-x",
            "contents": [
                {
                    "name": "parser_test.go",
                    "size": 1342,
                    "time_modified": 1700205662,
                    "permissions": "drwxr-xr-x"
                },
                {
                    "name": "parser.go",
                    "size": 1622,
                    "time_modified": 1700202950,
                    "permissions": "-rw-r--r--"
                },
                {
                    "name": "go.mod",
                    "size": 533,
                    "time_modified": 1699958000,
                    "permissions": "drwxr-xr-x"
                }
            ]
        },
        {
            "name": "token",
            "size": 4096,
            "time_modified": 1699954070,
            "permissions": "-rw-r--r--",
            "contents": [
                {
                    "name": "token.go",
                    "size": 910,
                    "time_modified": 1699954070,
                    "permissions": "-rw-r--r--"
                },
                {
                    "name": "go.mod",
                    "size": 66,
                    "time_modified": 1699944730,
                    "permissions": "drwxr-xr-x"
                }
            ]
        }
    ]
}

JSON_STRING = json.dumps(TEST_JSON_DATA)


def test_ls_basic():
    """Test basic ls output (without options)."""
    output = ls(JSON_STRING)
    expected = "LICENSE README.md ast go.mod lexer main.go parser token"
    assert output == expected


def test_ls_with_a_option():
    """Test ls with -a option to include hidden files."""
    output = ls(JSON_STRING, a_option=True)
    expected = ".gitignore LICENSE README.md ast go.mod lexer main.go parser token"
    assert output == expected


def test_ls_with_l_option():
    """Test ls with -l option for long listing format."""
    output = ls(JSON_STRING, l_option=True)
    expected_lines = "\n".join([
        "drwxr-xr-x 1071 2023-11-14 23:17:17 LICENSE",
        "drwxr-xr-x 83 2023-11-14 23:17:17 README.md",
        "-rw-r--r-- 4096 2023-11-14 23:24:25 ast",
        "drwxr-xr-x 60 2023-11-14 23:21:13 go.mod",
        "drwxr-xr-x 4096 2023-11-14 23:11:27 lexer",
        "-rw-r--r-- 74 2023-11-14 23:20:53 main.go",
        "drwxr-xr-x 4096 2023-11-17 00:41:02 parser",
        "-rw-r--r-- 4096 2023-11-14 23:07:50 token",
    ])
    for line in expected_lines:
        assert line in output


def test_ls_with_a_and_l_option():
    output = ls(JSON_STRING, a_option=True, l_option=True)
    expected_lines = "\n".join([
        "drwxr-xr-x 8911 2023-11-14 23:17:17 .gitignore",
        "drwxr-xr-x 1071 2023-11-14 23:17:17 LICENSE",
        "drwxr-xr-x 83 2023-11-14 23:17:17 README.md",
    ])
    for line in expected_lines:
        assert line in output


def test_ls_with_r_option():
    output = ls(JSON_STRING, r_option=True)
    expected = "token parser main.go lexer go.mod ast README.md LICENSE"
    assert output == expected


def test_ls_with_t_and_l_option():
    """Test ls with -t and -l options to sort by modification time and display detailed output."""
    output = ls(JSON_STRING, t_option=True, l_option=True, r_option=True)
    expected = (
        "drwxr-xr-x 4096 2023-11-17 08:21 parser\n"
        "-rw-r--r-- 4096 2023-11-14 11:28 ast\n"
        "drwxr-xr-x 4096 2023-11-14 10:51 lexer\n"
        "-rw-r--r-- 4096 2023-11-14 10:27 token\n"
        "-rw-r--r-- 74 2023-11-14 09:27 main.go\n"
        "drwxr-xr-x 60 2023-11-14 09:21 go.mod\n"
        "drwxr-xr-x 1071 2023-11-14 06:57 LICENSE\n"
        "drwxr-xr-x 83 2023-11-14 06:57 README.md")

    assert output.strip() == expected.strip()


def test_ls_with_invalid_filter():
    """Test ls with an invalid filter option."""
    output = ls(JSON_STRING, filter_option="invalid")
    expected = "Error: Invalid filter option. Use 'dir' for directories or 'file' for files."
    assert output == expected


def test_ls_with_path_option():
    """Test ls with a specified path."""
    output = ls(JSON_STRING, path="lexer")
    expected = "lexer_test.go go.mod lexer.go"
    assert output == expected


if __name__ == "__main__":
    pytest.main()