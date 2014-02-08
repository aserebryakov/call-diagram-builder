import hashlib
import re

class GraphNode:
    """Class containing all necessary information """
    """for the graph node"""
    stylestring = 'shape=box'
    indentlengh = 4

    def __init__(self, line):
        self.label  = ''
        self.node_id = ''
        self.indent = 0
        self.Parse(line)

    def CalculateIndent(self, line):
        return (len(re.findall(r'\s', line))//self.indentlengh)

    def Parse(self, line):
        self.label  = re.sub(r'\s*', '', line)
        self.node_id = 'node_' + hashlib.md5(self.label).hexdigest()
        self.indent = self.CalculateIndent(line)
         
    def GetIndent(self):
        return self.indent

    def GetDescription(self):
        description = self.node_id + '[' + self.stylestring + ', label=' + self.label + '];\n'
        return description 

    def GetId(self):
        return self.node_id

