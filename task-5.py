import matplotlib.pyplot as plt
import networkx as nx
import random

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.value < key:
            root.right = insert_node(root.right, key)
        else:
            root.left = insert_node(root.left, key)
    return root

def inorder_traversal(root, colors, color_map):
    if root:
        inorder_traversal(root.left, colors, color_map)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
        color_map[root.value] = color
        inorder_traversal(root.right, colors, color_map)

def breadth_first_traversal(root, colors, color_map):
    queue = [root]
    while queue:
        node = queue.pop(0)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
        color_map[node.value] = color
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def visualize_tree(root, traversal_type):
    colors = []
    color_map = {}
    
    if traversal_type == 'inorder':
        inorder_traversal(root, colors, color_map)
    elif traversal_type == 'breadth_first':
        breadth_first_traversal(root, colors, color_map)
    else:
        print("Invalid traversal type. Choose 'inorder' or 'breadth_first'.")
        return
    
    graph = nx.Graph()
    graph.add_node(root.value, color=color_map[root.value])
    visualize_tree_recursive(root, graph, color_map)
    
    positions = nx.spring_layout(graph)
    node_colors = [color_map[node] for node in graph.nodes()]
    
    nx.draw(graph, positions, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors)
    plt.show()

def visualize_tree_recursive(node, graph, color_map):
    if node.left:
        graph.add_node(node.left.value, color=color_map[node.left.value])
        graph.add_edge(node.value, node.left.value)
        visualize_tree_recursive(node.left, graph, color_map)
    if node.right:
        graph.add_node(node.right.value, color=color_map[node.right.value])
        graph.add_edge(node.value, node.right.value)
        visualize_tree_recursive(node.right, graph, color_map)

root_node = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root_node = insert_node(root_node, key)

visualize_tree(root_node, 'inorder') 
visualize_tree(root_node, 'breadth_first')
