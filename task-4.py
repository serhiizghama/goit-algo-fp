import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, value, color="skyblue"):
        self.left = None
        self.right = None
        self.value = value
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges_to_graph(graph, node, positions, x=0, y=0, depth=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2**depth
            positions[node.left.id] = (left_x, y - 1)
            add_edges_to_graph(graph, node.left, positions, x=left_x, y=y - 1, depth=depth + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2**depth
            positions[node.right.id] = (right_x, y - 1)
            add_edges_to_graph(graph, node.right, positions, x=right_x, y=y - 1, depth=depth + 1)
    return graph


def draw_binary_tree(root_node):
    tree_graph = nx.DiGraph()
    positions = {root_node.id: (0, 0)}
    tree_graph = add_edges_to_graph(tree_graph, root_node, positions)

    node_colors = [node_data["color"] for node_id, node_data in tree_graph.nodes(data=True)]
    node_labels = {node_id: node_data["label"] for node_id, node_data in tree_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree_graph, pos=positions, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors
    )
    plt.show()


def build_heap_tree(heap_array, index=0):
    if index < len(heap_array):
        node = TreeNode(heap_array[index])
        node.left = build_heap_tree(heap_array, 2 * index + 1)
        node.right = build_heap_tree(heap_array, 2 * index + 2)
        return node
    return None


def main():
    heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 6, 10, 8, 13, 14, 15, 17]
    heapq.heapify(heap_array)
    heap_tree_root = build_heap_tree(heap_array)
    draw_binary_tree(heap_tree_root)


if __name__ == "__main__":
    main()
