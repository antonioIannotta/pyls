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

    a_option = False
    l_option = False
    r_option = False
    h_option = False
    t_option = False
    filter_option = None
    path = None

    if "-A" in sys.argv:
        a_option = True

    if "-l" in sys.argv:
        l_option = True

    if "-r" in sys.argv:
        r_option = True

    if "-h" in sys.argv:
        h_option = True

    if "-t" in sys.argv:
        t_option = True

    for arg in sys.argv:
        if arg.startswith("--filter"):
            filter_option=arg.split("=")[1]

    for index, arg in enumerate(sys.argv[1:]):
        if not arg.startswith("-") and not arg.endswith(".json"):
            path = arg
            break


    print(ls(json_data, a_option, l_option, r_option, h_option, t_option, filter_option, path))


if __name__ == "__main__":
    main()