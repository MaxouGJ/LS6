#!/usr/bin/env python3

from Node import Node
from Edge import Edge

class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = set()

    def __repr__(self):
        return "Nodes : \n"+"\n".join([repr(self.nodes[n]) for n in self.nodes])+"\nEdges :\n"+"\n".join([repr(e) for e in self.edges])

    def add_node(self, n, color=None):
        if n in self.nodes :
            return self.nodes[n]
        else :
            new = Node(n, color)
            self.nodes[n] = new
            return new

    def add_edge(self, n1, n2, printcolor=None, label=None, data=None):
        node1 = self.add_node(n1)
        node2 = self.add_node(n2)
        self.edges.add(Edge(n1, n2, label, printcolor, data))
        node1.out_neighbors.append(node2)
        node2.in_neighbors.append(node1)

    def write(self, dotfile):
        f = open(dotfile+".dot", "w")
        f.write("digraph "+dotfile+" { \n")
        for e in self.edges :
            args =""
            if e.printcolor : args+="color="+e.printcolor
            if e.label :
                if args == "" : args += "label="+e.label
                else : args += ", label="+e.label
            f.write(e.src+" -> "+e.dest+" ["+args+"]\n")
        f.write("}\n")
        f.close()

if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A", "blue")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_edge("A", "B")
    graph.add_edge("A", "D")
    graph.add_edge("B", "C", "red", "Z")
    graph.add_edge("D", "C")
    graph.add_edge("E", "F")
    print(graph)
    graph.write("mongraph")
