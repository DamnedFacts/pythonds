import unittest
from .vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, n):
        return n in self.vertices

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        return None

    def add_edge(self, f, t, cost=0):
        if f not in self.vertices:
            self.add_vertex(f)

        if t not in self.vertices:
            self.add_vertex(t)

        self.vertices[f].add_neighbor(self.vertices[t], cost)

    def get_vertices(self):
        return self.vertices.keys()

    def graph(self, show_pred=False, show_arrows=False):
        from graphviz import Digraph
        
        gv = Digraph(graph_attr={'start': '2',
                                 'layout': 'neato',
                                 'overlap': 'scale',
                                 'splines': 'true'},
                     node_attr={'shape': 'circle',
                                'height': '.1'},
                     edge_attr={})

        if show_pred:
            for w in self.vertices.values():
                w_id = w.get_id()
                gv.node('node{0}'.format(w_id), '{0}'.format(w_id))
                if w.get_pred() and w.get_pred().get_id():
                    gv.attr('edge', dir="forward")
                    gv.edge('node{0}'.format(w_id),
                            'node{0}'.format(w.get_pred().get_id()))
        else:
            for v in self.vertices:
                v_id = self.vertices[v].get_id()
                gv.node('node{0}'.format(v_id), '{0}'.format(v_id))
                for w in self.vertices[v].connected_to.keys():
                    w_id = w.get_id()
                    gv.node('node{0}'.format(w_id), '{0}'.format(w_id))
                    if not show_arrows:
                        gv.attr('edge',  dir="none")
                    gv.edge('node{0}'.format(v_id),
                            'node{0}'.format(w_id))
        return gv

    def dfs(self):
        self.reset()

        for a_vertex in self:
            if a_vertex.get_color() == 'white':
                self.dfs_visit(a_vertex)

    def dfs_visit(self, start):
        start.set_color('gray')
        self.time += 1
        start.set_discovery(self.time)
        for _next in start.get_connections():
            if _next.get_color() == 'white':
                _next.set_pred(start)
                self.dfs_visit(_next)
                
        start.set_color('black')
        self.time += 1
        start.set_finish(self.time)

    def traverse(self, y):
        path = []
        x = y
        pred = x.get_pred()
        while x.get_pred():
            path.append(x)
            x = x.get_pred()
        return path

    def reset(self):
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_pred(None)

class GraphTests(unittest.TestCase):
    def setUp(self):
        self.t_graph = Graph()

    def test_make_graph(self):
        g_file = open("test.dat")
        for line in g_file:
            f_vertex, t_vertex = line.split('|')
            f_vertex = int(f_vertex)
            t_vertex = int(t_vertex)
            self.t_graph.add_edge(f_vertex, t_vertex)
        for i in self.t_graph:
            adj = i.getAdj()
            for k in adj:
                print(i, k)


if __name__ == '__main__':
    unittest.main()
