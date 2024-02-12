import os
import itertools
import time

def csv_to_adj_matrix(file_path):
    with open(file_path, 'r') as file:
        cities_loaded = False #Radi prvog retka, samo ucitamo gradove
        cities = []
        adj_matrix = []
        for line in file:
            temp_list = []
            elements = line.strip().split(',')
            if(cities_loaded == False):
                cities_loaded = True
                cities = elements[1:]
                continue
            for element in elements:
                if(element.isnumeric()):
                    temp_list.append(int(element))
                elif(element == "-"): #Udaljenost grada do samog sebe je 0
                    temp_list.append(0)

            adj_matrix.append(temp_list)

        return [cities, adj_matrix]

def brute_force(cities, adj_matrix):
    shortest_route = None
    min_distance = float('inf')

    for permutation in itertools.permutations(cities):
        route = list(permutation) + [permutation[0]] #Vracamo se u prvi grad (Tu su Nazivi gradova)
        current_distance = 0

        for i in range(len(route) - 1): #Prođemo redom po listi, ali vadimo indexe gradova
            from_city = cities.index(route[i]) #Indexe od grada jer iz matrice susjedstva ne vadimo po nazivu grada
            to_city = cities.index(route[i + 1])
            current_distance += adj_matrix[from_city][to_city]

        # Dodaj novu najkracu udaljenost
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route

    return shortest_route, min_distance

def print_list(list):
    for item in list:
        print(item)

def print_route(route):
    print("Shortest route:")
    print(' -> '.join(str(x) for x in route))

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj6/distance copy.csv'
    cities, adj_matrix = csv_to_adj_matrix(path)
    
    #print_list(cities)
    #print_list(adj_matrix)

    start = time.time()
    shortest_route, min_distance = brute_force(cities, adj_matrix)
    end = time.time()
    print("Time of execution: " + str(end - start) + " seconds.")
    print_route(shortest_route)
    print("Total distance:", min_distance)

if __name__ == "__main__":
    main()