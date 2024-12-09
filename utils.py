def read_json_content(json_file: str) -> str:
    with open(json_file, 'r') as file:
        return file.read()