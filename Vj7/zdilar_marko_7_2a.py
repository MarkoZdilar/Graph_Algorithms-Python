import networkx as nx
import numpy as np
import time
from math import sqrt

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
                cities.append([line[1], int(line[2]), int(line[3])])
            if(section == "arcs"):
                adj_matrix[int(line[0])][int(line[1])] = int(line[2]) #U fileu vec imamo zapisano oba puta (1-10-343, 10-1-343) pa je dovoljna samo ova linija

        return [cities, adj_matrix]

def euclid_distance(grad1, grad2):
    return sqrt((grad1[1] - grad2[1]) ** 2 + (grad1[2] - grad2[2]) ** 2) #Koristimo koordinate za izračun euklidske udaljenosti

def a_star_networkx(adj_matrix, start, goal, cities):
    G = nx.from_numpy_array(np.array(adj_matrix), create_using=nx.DiGraph)
                                                                    
    def heuristic(city_idx, _): #Kao heuristiku koristimo euklidsku udaljenost
        return euclid_distance(cities[city_idx], cities[goal])

    return nx.astar_path_length(G, start, goal, heuristic) #a_star_path_length trazi da heuristic funkcija prima 2 argumenta pa je zato nadodan i drugi ( _ ) nekoristeni

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj7/graph-airports-koord.net'
    cities, adj_matrix = read_pajek_to_adj_matrix(path)

    start_city = 0
    end_city = 1
    start = time.time()
    a_star_path_length = a_star_networkx(adj_matrix, start_city, end_city, cities)
    end = time.time()
    print("Time of execution (networkx): " + str(end - start) + " seconds.")
    print()
    print("A* algorithm - path length between " + cities[start_city][0] + " and " + cities[end_city][0] + " is " + str(a_star_path_length) + " km.")

if __name__ == "__main__":
    main()