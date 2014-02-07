import re
from FileLib import *
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

    def WriteHeader(self):
        self.__outfile.append('digraph stack {\n');

    def WriteFooter(self):
        self.__outfile.append('}');

    def EndLine(self):
        self.__outfile.append(';\n')

    def AddFirstNode(self, node):
        self.__outfile.append('    ' + node)

    def AddNextNode(self, node):
        self.__outfile.append(' -> ' + node)

    def AddBackTrace(self, stack, depth):
        self.AddFirstNode(stack.pop())

        for i in range(depth):
            self.AddNextNode(stack.pop())

        self.AddNextNode(stack[-1])
        self.EndLine()

        return stack;

    def ParseNodes(self):
        nodes = []
        for line in self.__infile.get_lines():
            if (re.sub(r'\s+', '', line) == ''):
                continue
            nodes.append(GraphNode(line))

        return nodes

    def WriteDescriptions(self, nodes):
        for node in nodes:
            self.__outfile.append('    ' + node.GetDescription())

    def Generate(self):
        nodes = self.ParseNodes()
        stack = [nodes[0]]
        prev_indent = stack[0].GetIndent()

        self.WriteHeader()
        self.WriteDescriptions(nodes)
        self.AddFirstNode(stack[0].GetDigest())

        for node in nodes[1:]:
            indent = node.GetIndent()

            if indent > prev_indent:
                stack.append(node)
                self.AddNextNode(stack[-1].GetDigest())
            elif indent < prev_indent:
                self.EndLine()
                for i in range(prev_indent - indent + 1):
                    stack.pop()
                self.AddFirstNode(stack[-1].GetDigest())
                stack.append(node)
                self.AddNextNode(stack[-1].GetDigest())
            else:
                stack.pop()
                self.AddNextNode(stack[-1].GetDigest())
                self.EndLine()
                self.AddFirstNode(stack[-1].GetDigest())
                stack.append(node)
                self.AddNextNode(stack[-1].GetDigest())

            prev_indent = indent

        self.EndLine()
        self.WriteFooter();

