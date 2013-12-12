from FileLib import *
import re

class GraphBuilder:
    """Class encapsulating building of the graph"""
    __infile = None
    __outfile = None
    __indent_value = 4

    def __init__(self, infile, outfile):
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

    def GetIndent(self, line):
        return (len(re.findall(r'\s', line))/self.__indent_value)

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


    def Generate(self):
        lines = self.__infile.get_lines()
        stack = [lines[0]]
        prev_indent = 0

        self.WriteHeader();
        self.AddFirstNode(lines[0])

        for line in lines[1:]:
            if (re.sub(r'\s+', '', line) == ''):
                continue

            indent = self.GetIndent(line)
            node = re.sub(r'\s*', '', line)

            if indent > prev_indent:
                stack.append(node)
                self.AddNextNode(stack[-1])
            elif indent < prev_indent:
                self.EndLine()
                for i in range(prev_indent - indent + 1):
                    stack.pop()
                self.AddFirstNode(stack[-1])
                stack.append(node)
                self.AddNextNode(stack[-1])
            else:
                stack.pop()
                self.AddNextNode(stack[-1])
                self.EndLine()
                self.AddFirstNode(stack[-1])
                stack.append(node)
                self.AddNextNode(stack[-1])

            prev_indent = indent

        self.EndLine()
        self.WriteFooter();

