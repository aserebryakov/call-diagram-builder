import sys
import argparse
from  graph_builder import GraphBuilder

NAME = "stack-graph-builder"
VERSION = "0.02"


def main(infile, outfile):
    print('Opening files...')
    graph_bldr = GraphBuilder(infile, outfile)
    print('Generating output...')
    graph_bldr.generate()
    print('Graph is saved in {0}'.format(outfile))

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help = "input file name")
    parser.add_argument("output_file", help = "output file name")

    args = parser.parse_args()

    print('{0} v{1}'.format(NAME, VERSION))

    sys.exit(main(args.input_file, args.output_file))
