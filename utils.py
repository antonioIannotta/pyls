import time

def read_json_content(json_file: str) -> str:
    """
    Read the file passed as input and return the content.
    :param json_file: the file to be read
    :return: the content of the file
    """
    with open(json_file, 'r') as file:
        return file.read()

def format_time(timestamp):
    """
    Convert Unix timestamp to a readable format.
    :param timestamp: the timestamp to be converted
    :return: the timestamp formatted
    """
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))


def format_bytes(size: int) -> str:
    """
    This function returns the size formatted in human-readable format
    :param size: the size to be formatted
    :return: the size formatted as a string
    """
    units = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    unit_index = 0

    # Convert to the appropriate unit (greater than 1023 bytes)
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"