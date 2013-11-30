from FileLib import *
import sys

NAME = "stack-graph-builder"
VERSION = "0.00"


def main(argv):
    print('{0} v{1}'.format(NAME, VERSION))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
