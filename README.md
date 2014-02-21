Call Diagram Builder
===================

This project purpose it to give to a developer an easy instrument for existing
source reverse engineering.

A lightweitht cross platform application written in Python allows relatively
easy build of call diargams in connection with other tools (any IDE and
Graphviz).

__NOTE:__ This tool does not parse sources. User need to build an input file by
himself and after that run a CDB. The received output must be rendered with
Graphviz DOT tool.


Requirements
------------
1. Pyhon 2.7 or higher
2. Graphviz


Example
-------
__Usage:__
```
cdb.py [-h] [-r] input_file output_file

positional arguments:
  input_file    input file name
  output_file   output file name

optional arguments:
  -h, --help    show this help message and exit

```

__Input file example:__

```
__main__
    parser.parse_args()
    main()
    GraphBuilder()
    graph_bldr.generate()
        parse_nodes()
        init_stack()
        write_header()
        write_descriptions()
        add_first_node()
        for node in nodes
            if indent > prev_indent
                add_next_node()
                else
                    end_line()
                    add_first_node()
                    add_next_node()
        end_line()
        write_footer()
    render_graph()
```
__NOTE:__  Each indentation level must be 4 spaces

__Output file__(quite ugly):

```
digraph stack {
    node_543fa9efacae37b4c698a94214cdf779[shape=box, label="__main__"];
    node_af6aeb779522175b1b66d4fe3cc54002[shape=box, label="parser.parse_args()"];
    node_ea83b916b3f52eec32ae6d54d59b4453[shape=box, label="main()"];
    node_5e9e5c8677031d0a5c4281953222adde[shape=box, label="GraphBuilder()"];
    node_04620bad6dd6f0cc4a315737e9bd4474[shape=box, label="graph_bldr.generate()"];
    node_ee6748ff45bc4d764dd7bbc2d850ffb5[shape=box, label="parse_nodes()"];
    node_991394a933c46548fea750a333fab064[shape=box, label="init_stack()"];
    node_42e03bfaddc19cf3a492c23d1a988c61[shape=box, label="write_header()"];
    node_74c51eb3af93f8ab7d88167dfe27210d[shape=box, label="write_descriptions()"];
    node_cc6db40ce35567d0d3b9b382edeb1649[shape=box, label="add_first_node()"];
    node_79538eb3e7d6d84f732a0541d00f043e[shape=box, label="for node in nodes"];
    node_46a3a620edf0ef33b9626b7e315d3e69[shape=box, label="if indent > prev_indent"];
    node_2ab61c93a613a4df1931bef2e0b8de35[shape=box, label="add_next_node()"];
    node_2954e92a9b4d0e998fe4893f8141649a[shape=box, label="else"];
    node_568935acb4d2fa915c1b88f70c667a58[shape=box, label="end_line()"];
    node_cc6db40ce35567d0d3b9b382edeb1649[shape=box, label="add_first_node()"];
    node_2ab61c93a613a4df1931bef2e0b8de35[shape=box, label="add_next_node()"];
    node_568935acb4d2fa915c1b88f70c667a58[shape=box, label="end_line()"];
    node_d097346eeaa288d106dd84757e5ebc1e[shape=box, label="write_footer()"];
    node_99d8b82af08954376af2379994278232[shape=box, label="render_graph()"];
    root -> node_543fa9efacae37b4c698a94214cdf779 -> node_af6aeb779522175b1b66d4fe3cc54002;
    node_543fa9efacae37b4c698a94214cdf779 -> node_ea83b916b3f52eec32ae6d54d59b4453;
    node_543fa9efacae37b4c698a94214cdf779 -> node_5e9e5c8677031d0a5c4281953222adde;
    node_543fa9efacae37b4c698a94214cdf779 -> node_04620bad6dd6f0cc4a315737e9bd4474 -> node_ee6748ff45bc4d764dd7bbc2d850ffb5;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_991394a933c46548fea750a333fab064;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_42e03bfaddc19cf3a492c23d1a988c61;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_74c51eb3af93f8ab7d88167dfe27210d;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_cc6db40ce35567d0d3b9b382edeb1649;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_79538eb3e7d6d84f732a0541d00f043e -> node_46a3a620edf0ef33b9626b7e315d3e69 -> node_2ab61c93a613a4df1931bef2e0b8de35;
    node_46a3a620edf0ef33b9626b7e315d3e69 -> node_2954e92a9b4d0e998fe4893f8141649a -> node_568935acb4d2fa915c1b88f70c667a58;
    node_2954e92a9b4d0e998fe4893f8141649a -> node_cc6db40ce35567d0d3b9b382edeb1649;
    node_2954e92a9b4d0e998fe4893f8141649a -> node_2ab61c93a613a4df1931bef2e0b8de35;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_568935acb4d2fa915c1b88f70c667a58;
    node_04620bad6dd6f0cc4a315737e9bd4474 -> node_d097346eeaa288d106dd84757e5ebc1e;
    node_543fa9efacae37b4c698a94214cdf779 -> node_99d8b82af08954376af2379994278232;
}
```

__Rendering example:__
```
dot output_file -Tpng -o call_diagram.png
```
__Note for Windows users:__
You will need to add path to Grapghviz\bin to PATH environment variable in order
to be able to use __dot__ the way it shown above.
