"""Vertex definition."""
import sys


class Vertex:
    """Vertex for use with Graph class."""

    def __init__(self, key):
        self.id = key
        self.connected_to = {}  # Adjacency "list"
        self.dist = sys.maxsize
        self.color = "white"
        self.pred = None
        self.disc = 0
        self.fin = 0

    def __str__(self):
        return f"{self.id} connected to: {[x.id for x in self.connected_to]}"

    def __repr__(self):
        return f"Vertex({self.id})"

    def add_neighbor(self, nbr, weight=0):
        """Add neighbor vertex."""
        self.connected_to[nbr] = weight

    def set_color(self, color):
        """Set marker color of vertex (for path marking)."""
        self.color = color

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime

    def get_finish(self):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_id(self):
        return self.id
