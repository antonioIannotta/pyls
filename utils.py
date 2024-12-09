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