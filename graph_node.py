from FileLib import *
import hashlib

class GraphNode:
    """Class containing all necessary information """
    """for the graph node"""
    stylestring = '[shape=box]'

    def __init__(self, label, intend):
        self.label  = label
        self.intend = indent
        self.digest = hashlib.md5(self.label).hexdigest()

    def WriteDescription(self, outfile):
        pass

    def WriteNode(self, outfile):
        pass

