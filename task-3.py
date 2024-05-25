import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Создание ориентированного графа
G = nx.DiGraph()

# Список ребер с весами
edges = [
    ("Киев", "Одесса", {"weight": 5}),
    ("Киев", "Харьков", {"weight": 3}),
    ("Одесса", "Харьков", {"weight": 2}),
    ("Одесса", "Львов", {"weight": 7}),
    ("Харьков", "Львов", {"weight": 4}),
    ("Львов", "Днепр", {"weight": 6}),
    ("Днепр", "Запорожье", {"weight": 4}),
    ("Львов", "Винница", {"weight": 3}),
    ("Винница", "Черновцы", {"weight": 5}),
    ("Запорожье", "Черновцы", {"weight": 2}),
    ("Винница", "Полтава", {"weight": 4}),
    ("Черновцы", "Полтава", {"weight": 6}),
    ("Полтава", "Сумы", {"weight": 3}),
]

# Добавление ребер в граф
G.add_edges_from(edges)

# Заданные позиции для узлов
node_positions = {
    "Киев": (0, -1),
    "Одесса": (1, 2),
    "Харьков": (1, -2),
    "Львов": (2, -1),
    "Днепр": (3, 2),
    "Запорожье": (4, -2),
    "Винница": (4, 1),
    "Черновцы": (5, 2),
    "Полтава": (5, -2),
    "Сумы": (6, -1),
}

# Функция для визуализации графа
def visualize_graph(graph, positions):
    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=8,
        font_color="black",
        font_weight="bold",
        edge_color="blue",
        width=2,
        arrowsize=30,
    )
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(
        graph, positions, edge_labels=edge_labels, font_color="red"
    )
    plt.show()

# Алгоритм Дейкстры для поиска кратчайших путей
def dijkstra(graph, start_node):
    shortest_distances = {node: float("infinity") for node in graph.nodes}
    shortest_distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph.get_edge_data(current_node, neighbor)["weight"]
            distance = shortest_distances[current_node] + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances

# Основная функция
def main():
    start_node = "Киев"

    shortest_paths = dijkstra(G, start_node)
    for node, distance in shortest_paths.items():
        if node != start_node:
            print(
                f"Найкоротший шлях з вершини {start_node} до вершини {node} = {distance}")

    visualize_graph(G, node_positions)


if __name__ == "__main__":
    main()
