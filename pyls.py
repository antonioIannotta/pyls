import sys

from commands.help_message import HELP_MESSAGE
from commands.ls_command import ls
from utils import read_json_content

if "--help" in sys.argv:
    print(HELP_MESSAGE)
    sys.exit(0)

def main():
    json_file: str = sys.argv[1]
    json_data: str = read_json_content(json_file)
    if len(sys.argv) == 2:
        print(ls(json_data))

    if "-A" in sys.argv:
        print(ls(json_data, a_option=True))

if __name__ == "__main__":
    main()