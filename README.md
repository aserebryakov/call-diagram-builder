Call Graph Builder
===================

The purpose of this script is to help in code revese engineering.
User by it self builds an input file, containing callstack state and script builds an ouput file in DOT format.

Requirements
------------
1. Pyhon interpreter
2. Graphviz installed in order to be able to render graph


Example
-------
__Usage:__
```
python sgb.py <input file> <output file>
```

__Input file:__

```
__main__
    main
        GraphBuilder
        Generate
            get_lines
            WriteHeader
            AddFirstNode
            lines_loop
                GetIndent
                if_block
                    indent_increased
                        AddNextNode
                    indent_decrased
                        AddBackTrace
                    nothing_changed
                        finish_the_line
            AddBackTrace
            WriteFooter
```
__NOTE:__  Each indentation level must be 4 spaces

__Output file__:

```
digraph stack {
    __main__ -> main -> GraphBuilder -> main;
    main -> Generate -> get_lines -> Generate;
    Generate -> WriteHeader -> Generate;
    Generate -> AddFirstNode -> Generate;
    Generate -> lines_loop -> GetIndent -> lines_loop;
    lines_loop -> if_block -> indent_increased -> AddNextNode;
    AddNextNode -> indent_increased -> if_block;
    if_block -> indent_decrased -> AddBackTrace;
    AddBackTrace -> indent_decrased -> if_block;
    if_block -> nothing_changed -> finish_the_line;
    finish_the_line -> nothing_changed -> if_block -> lines_loop -> Generate;
    Generate -> AddBackTrace -> Generate;
    Generate -> WriteFooter    WriteFooter -> Generate -> main -> __main__;
}
```
