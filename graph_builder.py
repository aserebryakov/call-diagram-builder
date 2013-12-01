from FileLib import *
import re

# Graph buiding pseudo code
#
# define stack
# push first line
# while not EOF
#   get last value in stack
#   get indent
#   if indent increased
#       push line to stack
#       add -> line to graph
#   else if indent decreased
#       end line with ";"
#       pop value from stack 
#       add this value to the beginning of new line
#       add value read from the line to graph
#   else
#       end line with ";"
#       get last value from the stack
#       add this value to the beginning of new line
#       add value read from the line to graph
#   endif
# end
#
# if stack is not empty
#   add ";" to graph line
#   start new line
#   pop element
#   add to the line
#
# while stack is not empty
#   pop element
#   add element to the line
# end
#
# add ";" to graph line
#


class GraphBuilder:
    """Class incapsulating building of the graph"""
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

    def AddNextNode(self, node):
       self.__outfile.append(' -> ' + node)

    def AddFirstNode(self, node):
       self.__outfile.append('    ' + node)

    def EndLine(self):
       self.__outfile.append(';\n')

    def Generate(self):
        lines = self.__infile.get_lines()
        stack = [lines[0]]
        prev_indent = 0

        self.WriteHeader();
        self.AddFirstNode(lines[0])

        for line in lines[1:]:
            indent = self.GetIndent(line)

            if indent > prev_indent:
                stack.append(re.sub(r'\s*', '', line))
                self.AddNextNode(stack[-1])
            elif indent < prev_indent:
                self.EndLine()
                stack.pop()
                self.AddFirstNode(re.sub(r'\s*', '', line))
                self.AddNextNode(stack[-1])
            else:
                self.EndLine()
                self.AddFirstNode(re.sub(r'\s*', '', line))
                self.AddNextNode(stack[-1])

            prev_indent = indent

        if len(stack) > 0:
             self.EndLine()
             self.AddFirstNode(stack.pop())

        while len(stack) > 0:
             self.AddNextNode(stack.pop())

        self.EndLine();
        self.WriteFooter();



