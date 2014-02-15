# This module incapsulates work with an input file
#
# InFile:
#   variables:
#   - descriptor
#   - content
#   - lines
#   methods:
#   - get_content
#   - get_lines

import sys


class InFile:
    """InFile class"""

    def __init__(self, filename):
        """Constructor"""
        self.__descriptor = None
        self.__content = None
        self.__lines = []
        try:
            self.__descriptor = open(filename, "r")
        except IOError as e:
            print("I/O error {0}: {1}".format(e.errno, e.strerror))
            raise IOError

        self.__content = self.__descriptor.read()
        self.__lines = self.__content.splitlines()
        self.__descriptor.close()

    @property
    def content(self):
        return self.__content

    @property
    def lines(self):
        """Returns file content as a list of strings""" 
        return self.__lines
