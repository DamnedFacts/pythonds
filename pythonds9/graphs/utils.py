def viz_graph(g, show_pred=False, show_arrows=False):
    from graphviz import Digraph
    
    gv = Digraph(graph_attr={'start': '2',
                             'layout': 'neato',
                             'overlap': 'scale',
                             'splines': 'true'},
                 node_attr={'shape': 'circle',
                            'height': '.1'},
                 edge_attr={})

    if show_pred:
        for w in g.vertices.values():
            w_id = w.get_id()
            gv.node('node{0}'.format(w_id), '{0}'.format(w_id))
            if w.get_pred() and w.get_pred().get_id():
                gv.attr('edge', dir="forward")
                gv.edge('node{0}'.format(w_id),
                        'node{0}'.format(w.get_pred().get_id()))
    else:
        for v in g.vertices:
            v_id = g.vertices[v].get_id()
            gv.node('node{0}'.format(v_id), '{0}'.format(v_id))
            for w in g.vertices[v].connected_to.keys():
                w_id = w.get_id()
                gv.node('node{0}'.format(w_id), '{0}'.format(w_id))
                if not show_arrows:
                    gv.attr('edge',  dir="none")
                gv.edge('node{0}'.format(v_id),
                        'node{0}'.format(w_id))
    return gv
