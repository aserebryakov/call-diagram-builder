import re
from filelib import *
from graph_node import GraphNode

class GraphBuilder:
    """Class encapsulating building of the graph"""

    def __init__(self, infile, outfile):
        self.__infile = None
        self.__outfile = None
        self.__indent_value = 4

        try:
            self.__infile = InFile(infile)
        except IOError:
            print('Can\'t open input file')
            raise IOError

        try:
            self.__outfile = OutFile(outfile)
        except IOError:
            print('Can\'t open output file')
            raise IOError

    def write_header(self):
        self.__outfile.append('digraph stack {\n');

    def write_footer(self):
        self.__outfile.append('}');

    def end_line(self):
        self.__outfile.append(';\n')

    def add_first_node(self, node):
        self.__outfile.append('    ' + node)

    def add_next_node(self, node):
        self.__outfile.append(' -> ' + node)

    def parse_nodes(self):
        nodes = []
        for line in self.__infile.lines:
            if (re.sub(r'\s+', '', line) == ''):
                continue
            nodes.append(GraphNode(line))

        return nodes

    def write_descriptions(self, nodes):
        for node in nodes:
            self.__outfile.append('    {0}'.format(node.get_description()))

    def init_stack(self):
        node = GraphNode("root")
        node._GraphNode__node_id = "root"
        node._GraphNode__indent = -1
        return [node]

    def generate(self):
        nodes = self.parse_nodes()
        stack = self.init_stack()
        prev_indent = -1

        self.write_header()
        self.write_descriptions(nodes)
        self.add_first_node("root")

        for node in nodes:
            indent = node.indent

            if indent > prev_indent:
                stack.append(node)
                self.add_next_node(stack[-1].node_id)
            else:
                self.end_line()
                for i in range(prev_indent - indent + 1):
                    stack.pop()
                self.add_first_node(stack[-1].node_id)
                stack.append(node)
                self.add_next_node(stack[-1].node_id)

            prev_indent = indent

        self.end_line()
        self.write_footer();

