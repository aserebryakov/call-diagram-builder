import sys
from  graph_builder import GraphBuilder

NAME = "stack-graph-builder"
VERSION = "0.01"


def main(argv):
    print('{0} v{1}'.format(NAME, VERSION))
    graph_bldr = GraphBuilder(argv[0], argv[1])
    graph_bldr.Generate();

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
