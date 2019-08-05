from ..basic import Stack
from graphviz import Digraph

def viz_tree(r):
    stack = Stack()
    g = Digraph(node_attr={'shape': 'record', 'height': '.1'})
    _id = 0
    current_node = r
    leftward = True
    current_root_num = 0
    
    while True:
        if current_node:
            stack.push((_id, current_node))
            node_val = current_node.get_root_val()
            if isinstance(node_val, str) and node_val in ["|", "<", ">", "\"", "'"]:
                node_val = node_val.replace(node_val, "\\" + node_val)
            g.node(f'node{_id}', f'<f0>|<f1> {node_val} (#{_id})|<f2> ')
            if _id >= 1:
                g.edge('node{0}:f{1}'.format(current_root_num, 0 if leftward else 2),
                       'node{0}:f1'.format(_id))
                
            leftward = True
            current_node = current_node.get_left_child()  # left
            current_root_num = _id
            _id += 1

        if current_node is None and not stack.is_empty():
            count, popped_node = stack.pop()
            if popped_node.get_right_child():
                current_root_num = count
                current_node = popped_node.get_right_child()  # right
                leftward = False
            
        if current_node is None and stack.is_empty():
            break

    return g
