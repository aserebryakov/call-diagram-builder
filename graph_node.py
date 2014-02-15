import hashlib
import re

class GraphNode:
    """Class containing all necessary information """
    """for the graph node"""
    stylestring = 'shape=box'
    indentlengh = 4

    def __init__(self, line):
        self.__label  = ''
        self.__node_id = ''
        self.__indent = 0
        self.__parse(line)

    def calculate_indent(self, line):
        match = re.match(r'\s+', line)
        indent = 0 

        if match is not None:
            indent = len(re.findall(r'\s', match.string))//self.indentlengh

        return indent

    def __parse(self, line):
        self.__label  = re.sub(r'\s*', '', line, 1)
        self.__node_id = 'node_' + hashlib.md5(self.__label).hexdigest()
        self.__indent = self.calculate_indent(line)
         
    @property
    def node_id(self):
        return self.__node_id

    @property
    def indent(self):
        return self.__indent

    def get_description(self):
        description = self.__node_id + '[' + self.stylestring + ', label="' + self.__label + '"];\n'
        return description 

