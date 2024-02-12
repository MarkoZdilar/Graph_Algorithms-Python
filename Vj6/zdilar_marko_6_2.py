from zdilar_marko_6_1 import csv_to_adj_matrix, print_route, print_list
import time

def nearest_neighbor_algorithm(cities, adj_matrix):
    visited = [cities[0]]
    while len(visited) < len(cities):
        last_visited = visited[-1] #Zadnji posjeceni (Najblizi u odnosu na prethodnog)
        last_index = cities.index(last_visited)
        
        # Prema uputama - Trazi se najblizi NEPOSJECENI susjed u odnosu na trenutni
        nearest_neighbor = None
        min_distance = float('inf')
        for i in range(len(cities)):
            distance = adj_matrix[last_index][i]
            if distance < min_distance and cities[i] not in visited: #Ako je grad blizi i nije posjecen
                nearest_neighbor = cities[i]
                min_distance = distance

        # Dodajemo najblizeg u posjecene
        visited.append(nearest_neighbor)

    # Zadnji grad mora biti pocetni
    visited.append(visited[0])

    distance = 0

    #Isto zbrajanje udaljenosti za pronađenu rutu (radi kao i kod brute force)
    for i in range(len(visited) - 1): #Prođemo redom po listi, ali vadimo indexe gradova
        from_city = cities.index(visited[i]) #Indexe od grada jer iz matrice susjedstva ne vadimo po nazivu grada
        to_city = cities.index(visited[i + 1])
        distance += adj_matrix[from_city][to_city]

    return [visited, distance]

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj6/distance.csv'
    cities, adj_matrix = csv_to_adj_matrix(path)
    
    #print(cities)
    #print_list(adj_matrix)
    start = time.time()
    route, distance = nearest_neighbor_algorithm(cities, adj_matrix)
    end = time.time()
    print("Time of execution: " + str(end - start) + " seconds.")
    print_route(route)
    print("Distance: " + str(distance))

if __name__ == "__main__":
    main()