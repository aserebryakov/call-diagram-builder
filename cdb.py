import sys
import argparse
import re
import subprocess
from  graph_builder import GraphBuilder

NAME = 'call-diagram-builder'
VERSION = '0.02'

def render_graph(output_file):
    result = 1

    try:
        image_name = re.sub(r'\..*', '.png', output_file)
        args = ['dot', output_file, '-Tpng', '-o', image_name]
        result = subprocess.call(args)

        if(result == 0):
            print('Graph is rendered to {0}'.format(image_name))

    except:
        print('ERROR: Cannot run DOT. Please check your PATH')

    return result


def main(args):
    result = 0

    print('Opening files...')
    graph_bldr = GraphBuilder(args.input_file, args.output_file)
    print('Generating output...')
    graph_bldr.generate()
    print('Graph is saved in {0}'.format(args.output_file))

    if(args.render):
        result = render_graph(args.output_file)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help = 'input file name')
    parser.add_argument('output_file', help = 'output file name')
    parser.add_argument('-r', '--render', help = 'call DOT to render graph after generation', \
                        action = 'store_true')

    args = parser.parse_args()

    print('{0} v{1}'.format(NAME, VERSION))

    sys.exit(main(args))
