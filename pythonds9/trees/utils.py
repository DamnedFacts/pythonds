from ..basic.stack import Stack
from .binary_tree import BinaryTree
from .bst import BinarySearchTree, TreeNode
from graphviz import Digraph


def viz_tree_list(r):
    """Visualize a list-based tree data structure
    
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is None
    4) If current is None and stack is not empty then 
         a) Pop the top item from stack.
         b) Print the popped item, set current = popped_item->right 
         c) Go to step 3.
    5) If current is None and stack is empty then we are done.
    """
    stack = Stack()
    g = Digraph(node_attr={'shape': 'record', 'height': '.1'})
    _id = 0
    current_node = r
    leftward = True
    current_root_num = 0

    while True:
        if current_node:
            stack.push((_id, current_node))
            
            g.node('node{0}'.format(_id), '<f0> |<f1> {0} (#{1})|<f2> '.format(current_node[0], _id))
            if _id >= 1:
                g.edge('node{0}:f{1}'.format(current_root_num, 0 if leftward else 2),
                       'node{0}:f1'.format(_id))

            leftward = True
            current_node = current_node[1]  # left
            current_root_num = _id
            _id += 1

        if current_node == [] and not stack.is_empty():
            count, popped_node = stack.pop()
            if popped_node[2]:
                current_root_num = count
                current_node = popped_node[2]  # right
                leftward = False
            
        if current_node == [] and stack.is_empty():
            break

    return g

def viz_tree(r):
    """Visualize a BinaryTree or BinarySearchTree Tree"""
    stack = Stack()
    g = Digraph(node_attr={'shape': 'record', 'height': '.1'})
    _id = 0
    
    if isinstance(r, BinaryTree):
        current_node = r
    elif isinstance(r, BinarySearchTree):
        current_node = r.root  # root is a TreeNode object!
        
    leftward = True
    current_root_num = 0

    while True:
        if current_node:
            stack.push((_id, current_node))
            
            if isinstance(current_node, BinaryTree):
                g.node(f'node{_id}',
                   f'<f0>|<f1> {current_node.key}|<f2> ')
            elif isinstance(current_node, TreeNode):
                g.node(f'node{_id}',
                   f'<f0>|<f1> {current_node.key}:{current_node.payload}|<f2> ')
            elif isinstance(current_node, AVLTreeNode):
                g.node(f'node{_id}',
                       f'<f0>|<f1> {current_node.key}:{current_node.payload} ({current_node.balance_factor})|<f2> ')

            if _id >= 1:
                g.edge(f'node{current_root_num}:f{0 if leftward else 2}',
                       f'node{_id}:f1')

            leftward = True
            current_node = current_node.left_child  # left
            current_root_num = _id
            _id += 1

        if current_node is None and not stack.is_empty():
            count, popped_node = stack.pop()
            if popped_node.right_child:
                current_root_num = count
                current_node = popped_node.right_child  # right
                leftward = False

        if current_node is None and stack.is_empty():
            break

    return g
