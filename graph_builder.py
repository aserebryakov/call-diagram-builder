from FileLib import *

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
    
