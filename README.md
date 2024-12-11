# `pyls` – A Command-Line File Listing Tool

`pyls` is a command-line tool that mimics the functionality of the `ls` command, allowing you to list and format file or directory contents with various options like sorting, filtering, and displaying hidden files.

## Features

- List files and directories.
- Display detailed information with the `-l` option.
- Show hidden files with the `-A` option.
- Sort files by modification time with the `-t` option.
- Reverse the sorting order with the `-r` option.
- Display human-readable sizes with the `-h` option.
- Filter by file type using `--filter` (supports `dir` or `file`).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/antonioIannotta/pyls.git
   cd pyls
   ```
2. **Create a virtual environment (optional but recommended)**:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies from requirements.txt**:

Install the required dependencies using the following command.
```bash
python3 -m venv venv
pip install -r requirements.txt
```

4. **Make the script executable**:
```bash
chmod +x pyls.py
```

# Usage
## Basic Syntax

```bash
python -m pyls data.json [OPTIONS] [PATH] [--filter=<dir|file>]
```
- OPTIONS: Command-line options (e.g., -l, -A).
- PATH: The path to the directory you want to list (optional).
- data.json: The JSON file representing the file system.

## Command line options

| Option                         | Description                                        |
|--------------------------------|----------------------------------------------------|
| -A	                            | Include hidden files (those starting with .)       |
| -l                             | 	Use a long listing format (detailed info)         |
| -r	                            | Reverse the order of the sorting                   |
| -h	                            | Display file sizes in human-readable format (e.g., KB) |
| -t	                            | Sort by modification time, newest first            |
| --filter=dir                   | 	Show only directories                             |
| --filter=file| 	Show only files                                   |


## Examples

1. Basic listing with details:
```bash
python -m pyls data.json -l
```
2. Include hidden files
```bash
python -m pyls data.json -A
```
3. List a specific path within the JSON file
```bash
python -m pyls data.json -l parser
```