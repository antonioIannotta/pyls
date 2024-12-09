import sys

from help_message import HELP_MESSAGE

if "--help" in sys.argv:
    print(HELP_MESSAGE)
    sys.exit(0)

def main():
    return