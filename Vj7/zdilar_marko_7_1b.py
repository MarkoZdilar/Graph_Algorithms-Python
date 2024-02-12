from zdilar_marko_7_1a import read_pajek_to_adj_matrix
import networkx as nx
import numpy as np
import time

def bellman_ford_with_networkx(adj_matrix, start_node):
    graph = nx.from_numpy_array(np.array(adj_matrix), create_using=nx.DiGraph) #Usmjereni graf (dict)
    lengths = nx.single_source_bellman_ford_path_length(graph, start_node) #Najkraći put koristeći bellman ford
    return lengths

def print_distances(distances, cities, start_city):
    for city_index, distance in distances.items():
        print(f"Shortest path from {cities[start_city]} to {cities[city_index]} is {distance}.")

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj7/graph-airports-koord.net'
    cities, adj_matrix = read_pajek_to_adj_matrix(path)

    start_city = 0

    start = time.time()
    distances = bellman_ford_with_networkx(adj_matrix, start_city)
    end = time.time()
    print("Time of execution (networkx): " + str(end - start) + " seconds.")
    print_distances(distances, cities, start_city)

if __name__ == "__main__":
    main()