import networkx as nx
import numpy as np
import time

def read_pajek_to_adj_matrix(file_path):
    with open(file_path, 'r') as file:
        section = None
        cities = []
        adj_matrix = []
        for line in file:
            if(line.lower().startswith("*vertices")):
                section = "vertices"
                continue
            elif(line.lower().startswith("*arcs")):
                section = "arcs"
                #Punimo kvadratnu matricu nulama kada sve gradove prođemo
                for _ in range (len(cities)):
                    row = []
                    for _ in range (len(cities)):
                        row.append(0)
                    adj_matrix.append(row)
                continue
            line = line.split()
            if(section == "vertices"):
                cities.append(line[1])
            if(section == "arcs"):
                adj_matrix[int(line[0])][int(line[1])] = int(line[2]) #U fileu vec imamo zapisano oba puta (1-10-343, 10-1-343) pa je dovoljna samo ova linija

        return [cities, adj_matrix]

def dijkstra_with_networkx(adj_matrix, start_node):
    graph = nx.from_numpy_array(np.array(adj_matrix), create_using=nx.DiGraph) # Ovo napravi usmjereni graf (Dict)

    lengths = nx.single_source_dijkstra_path_length(graph, start_node) #Izračunavanje najkraćeg puta do svakog čvora pomoću dijkstra algoritma

    return lengths

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj7/graph-airports-koord.net'
    cities, adj_matrix = read_pajek_to_adj_matrix(path)
    start_city = 0

    print("\nDijkstra networkx:")
    start = time.time()
    shortest_paths = dijkstra_with_networkx(adj_matrix, start_city)
    end = time.time()
    print("Time of execution (networkx): " + str(end - start) + " seconds.")

    for city_index, distance in shortest_paths.items():
        print(f"Shortest path from {cities[start_city]} to {cities[city_index]} is {distance}.")
    print()

if __name__ == "__main__":
    main()