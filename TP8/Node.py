#!/usr/bin/env python3

class Node:

    def __init__(self, name, color=None):
        self.name = name
        self.printcolor = color
        self.in_neighbors = []
        self.out_neighbors = []

    def __repr__(self):
        n = self.name
        if self.printcolor != None : n += " : "+self.printcolor
        return n+"\nin:"+"".join([s.name for s in self.in_neighbors])+"\nout : "+" ".join([s.name for s in self.out_neighbors])
