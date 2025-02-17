import time
import matplotlib.pyplot as plt

# DFS
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()  # Backtrack
    return None

# DLS
def dls(graph, start, goal, depth_limit, depth=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    if depth >= depth_limit:
        path.pop()  # Backtrack
        return None

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, depth_limit, depth + 1, visited, path)
            if result:
                return result

    path.pop()  # Backtrack
    return None

# IDDFS
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        result = dls(graph, start, goal, depth, 0, visited, path)
        if result:
            return result
    return None

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start, goal = 'A', 'F'

# Medir el tiempo y ejecutar DFS
start_time = time.time()
dfs_path = dfs(graph, start, goal)
dfs_time = time.time() - start_time
print("DFS:", dfs_path)
print("DFS Tiempo de ejecución:", dfs_time)

# Medir el tiempo y ejecutar DLS
start_time = time.time()
dls_path = dls(graph, start, goal, 2)
dls_time = time.time() - start_time
print("DLS (límite 2):", dls_path)
print("DLS Tiempo de ejecución:", dls_time)

# Medir el tiempo y ejecutar IDDFS
start_time = time.time()
iddfs_path = iddfs(graph, start, goal, 3)
iddfs_time = time.time() - start_time
print("IDDFS:", iddfs_path)
print("IDDFS Tiempo de ejecución:", iddfs_time)

# Visualización de los caminos con matplotlib
def plot_path(graph, path, title):
    # Dibujar el grafo
    plt.figure(figsize=(6, 6))
    positions = {
        'A': (0, 1), 'B': (-1, 0), 'C': (1, 0),
        'D': (-2, -1), 'E': (0, -1), 'F': (2, -1)
    }
    for node, (x, y) in positions.items():
        plt.text(x, y, node, fontsize=12, ha='center', color='black')
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            plt.plot([positions[node][0], positions[neighbor][0]],
                     [positions[node][1], positions[neighbor][1]], 'k-', lw=1)
    
    # Resaltar el camino
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i+1]
        plt.plot([positions[node1][0], positions[node2][0]],
                 [positions[node1][1], positions[node2][1]], 'ro-', lw=3)
    
    plt.title(title)
    plt.axis('off')
    plt.show()

# Graficar los caminos encontrados
plot_path(graph, dfs_path, "DFS Caminando")
plot_path(graph, dls_path, "DLS Caminando")
plot_path(graph, iddfs_path, "IDDFS Caminando")
