Script to generate connected graphs
===================================

A tool to generate graphs, based on the [Barabási–Albert (BA) model](http://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model).
You can use this to generate test data that resembles relations on a social graph.


Usage
-----
The script accepts the following argumens
* m  How many edges to create for each node (default 10)
* n  Number of nodes in the graph (default 1000)
* s  The format string (default {a}:{b})
* u  If present, it will generates an unidirectional graph (default bidirectional graph).

Note that, the script generate edges in pairs by default, e.g., a->b, b->a. That is bidirectional.
So a `-m` value of 10, it will actually create a network whose average # of edges per node is 20.
You can use `-u` to generates an unidirectional graph.

Use `-s` to specify your output format, most likely some sort of CSV to import into your DB;
format is the one used for Python's string formatting.

It will print the generated distribution (the distribution of node degrees) at the end.

Example
-------

Runnning time is acceptable for medium-sized networks. On a modest notebook, you can expect

	time python3 ba_graph.py -m 50 -n 200000 -s "{a};{b}" > data.csv
	real    20m41.900s
	user    20m30.190s
	sys     0m3.980s

that is 20' to generate 200000 nodes and 20000000 (twenty million) edges.

For the above example, the resulting node degree distribution is:

![distribution](https://raw.githubusercontent.com/MWPG/ba_graph/master/doc/distribution.png)
(note the log10 scale)

Have fun!
