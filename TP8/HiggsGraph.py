#!/usr/bin/env python3

from Node import Node
from Edge import Edge
from Graph import Graph
import sys
import time

class HiggsGraph(Graph):

    def __init__(self, fichier):
        Graph.__init__(self)#équivalent de super
        f = open(fichier)
        for l in f.readlines():
            s = l.split(" ")
            self.nodes[s[0]] = Node(s[0])
            self.nodes[s[1]] = Node(s[1])
            color = None
            if s[3] == "RT" : color = "red"
            elif s[3] == "MT" : color = "blue"
            elif s[3] == "RE" : color = "green"
            self.edges.add(Edge(s[0], s[1], data=time.localtime(int(s[2])), color=color))
        f.close()

if __name__ == "__main__":

    g = HiggsGraph(sys.argv[1])
    g.write("twitter")
    #print(g)
