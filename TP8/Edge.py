#!/usr/bin/env python3

class Edge:

    def __init__(self, src, dest, label=None, color=None, data=None):
        self.src = src
        self.dest = dest
        self.label = label
        self.printcolor = color
        self.data = data

    def __repr__(self):
        e = ""
        if self.label : e += self.label+" : "
        e += self.src+" -> "+self.dest
        if self.printcolor : e += ", "+self.printcolor
        if self.data : e += ", "+str(self.data)
        return e
