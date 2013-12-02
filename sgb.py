import sys
from  graph_builder import GraphBuilder

NAME = "stack-graph-builder"
VERSION = "0.01"


def main(argv):
    print('{0} v{1}'.format(NAME, VERSION))

    if len(argv) != 2:
        print('Usage: sgb <input> <output>')
        return 0

    print('Opening files...')
    graph_bldr = GraphBuilder(argv[0], argv[1])
    print('Generating output...')
    graph_bldr.Generate();
    print('Graph is saved in {0}'.format(argv[1]))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
