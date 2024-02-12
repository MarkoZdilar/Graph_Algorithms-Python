from zdilar_marko_7_2a import read_pajek_to_adj_matrix, euclid_distance
import time
import heapq
import networkx as nx
import numpy as np

def greedy_bfs_networkx(adj_matrix, start, goal, cities):
    graph = nx.from_numpy_array(np.array(adj_matrix), create_using=nx.DiGraph)

    def heuristic(city_idx):
        return euclid_distance(cities[city_idx], cities[goal])

    visited = set()
    queue = [(0, start)]  # Uključujemo početnu udaljenost (0) i početni grad
    heapq.heapify(queue)

    while queue:
        acc_distance, current = heapq.heappop(queue)
        if current == goal:
            return acc_distance  # Vraćamo ukupnu udaljenost kada dođemo do ciljnog grada
        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    new_distance = acc_distance + graph[current][neighbor]['weight']  # Dodajemo težinu bridova
                    heapq.heappush(queue, (new_distance + heuristic(neighbor), neighbor))
    
    return float('inf')  # Ako put nije pronađen, vraćamo beskonačno


def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj7/graph-airports-koord.net'
    cities, adj_matrix = read_pajek_to_adj_matrix(path)

    start_city = 0
    end_city = 1
    start = time.time()
    a_star_path_length = greedy_bfs_networkx(adj_matrix, start_city, end_city, cities)
    end = time.time()
    print("Time of execution (networkx): " + str(end - start) + " seconds.")
    print()
    print("Greedy BFS algorithm - path length between " + cities[start_city][0] + " and " + cities[end_city][0] + " is " + str(a_star_path_length) + " km.")

if __name__ == "__main__":
    main()