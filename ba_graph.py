#! /usr/bin/env python3
#! -*- coding:utf-8 -*-
#This Python file uses the following encoding: utf-8
#  revised to use Python-3 M.W.


"""
Generate a graph using the Barabase-Albert method.
http://en.wikipedia.org/wiki/Barabási–Albert_mode

IMPORTANT!
Generated graph is bidirectional,  edges are always generated in pairs a->b and b->a

Revised to generates both bidirectional graphes and unidirectional ones. M.W.

Algorithm:
     Nodes resides on a set of buckets,  each bucket corresponding to the degree of the nodes it contains.
     The probability of choosing a given bucket is  bucket degree * nodes in the bucket / total # edges in graph
     Once choosen a bucket, each member has the same probability of being choosed.  The choosed node is moved to
     a higher degree, and the algorithm continues.

By P.P (Pablo Polvorin). M.W. (Mogei Wang) revised
"""


import getopt
import sys
import random


# Default values
m = 10
n = 1000
s = "{a}:{b}"
# d = False # true to print distribution
u = False # true to generates unidirectional graphes


def usage():
    print("-m Edges\t -Number of edges to add per nodes")
    print("-n Nodes\t -Number of nodes")
    print("-s \"format string\"\t -Format string. Use {a} and {b}")
    # print("-d\t Print distribution at the end ")
    print("-u\t unidirectional or bidirectional [the later is default]")


try:
    opts, args = getopt.getopt(sys.argv[1:], 'm:n:s:u') # 'd' is removed
    for k,v in opts:
        if k == "-m": m = int(v)
        if k == "-n": n = int(v)
        if k == "-s": s = v
        # if k == "-d": d = True
        if k == "-u": u = True
except getopt.GetoptError as err:
    print(str(err))
    usage()
    sys.exit(2)


edges_count = 0.0
nodes_map = {} # edge degree -> [node_name()]


def output(a,b):
    print(s.format(a = a, b = b))
    if (not u): print(s.format(a = b, b = a))


def add_to(degree, node):
    global nodes_map
    if not degree in nodes_map: nodes_map[degree] = []
    nodes_map[degree].append(node)


def remove_from(degree, list, index):
    global nodes_map
    del list[index]
    if not list: del nodes_map[degree]


def generate(initials, iterations, edges):
    global edges_count
    global nodes_map
    shuffled_nodes = range(iterations)
    #random.shuffle(shuffled_nodes)
    for i in range(initials):
        add_to(2, shuffled_nodes[i])
        if i +1 == initials: output(shuffled_nodes[i], shuffled_nodes[1])
        else: output(shuffled_nodes[i], shuffled_nodes[i+1])
        edges_count = edges_count +2 #edges are bidirectional

    for i in shuffled_nodes[initials:]:
        new = i
        used = {}
        for k in range(edges):
            choosed_index = None
            choosed_list = None
            choosed_degree = None
            choosed = None
            while (choosed == None) or (choosed in used):
                r = random.random()
                accum = 0.0 #important, must not be an integer
                for degree,nodes in nodes_map.items():
                    subtotal = degree * len(nodes)
                    accum = accum + float(subtotal) / edges_count
                    if r <= accum :
                        choosed_list = nodes
                        choosed_index =  random.randrange(len(nodes))
                        choosed = choosed_list[choosed_index]
                        choosed_degree = degree
                        break

            output(new, choosed)
            edges_count = edges_count +2
            remove_from(choosed_degree, choosed_list, choosed_index)
            add_to(choosed_degree +1, choosed)
            used[choosed] = True
        add_to(edges, new)


generate(m, n, m)
# if (not d): exit()
print('\n')
for k,v in nodes_map.items(): print("# %s\t%s " % (k, len(v)))
