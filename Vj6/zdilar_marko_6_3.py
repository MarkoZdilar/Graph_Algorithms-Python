from zdilar_marko_6_1 import csv_to_adj_matrix, print_list
import time

def add_edge_to_graph(graph, edge):
    u, v, weight = edge
    if u not in graph:
        graph[u] = []
    graph[u].append((v, weight))

def has_cycle_dfs(graph, node, visited, parent):
    visited[node] = True
    for neighbour, _ in graph.get(node, []): #Ako key "node" ne postoji u graphu, vrati []
        if not visited[neighbour]:
            if has_cycle_dfs(graph, neighbour, visited, node):
                return True
        elif neighbour != parent:
            return True
    return False

def sorted_neighbors_algorithm(edges, num_cities):
    edges.sort(key=lambda x: x[2])
    graph = {}
    for edge in edges:
        u, v, _ = edge
        # Dodaj brid samo ako ne stvara vrh stupnja većeg od 2
        if len(graph.get(u, [])) < 2 and len(graph.get(v, [])) < 2: #Ako ne ide ni iz pocetnog ni iz zavrsnog grada 2 ili vise drugih gradova
            add_edge_to_graph(graph, edge)
            visited = [False] * num_cities
            if has_cycle_dfs(graph, u, visited, -1) and len(graph) < num_cities:
                # Ukloni brid ako stvara ciklus prije nego što su SVI gradovi povezani
                graph[u].pop() #Pop jer se radi o zadnje dodanom
    return graph

def adjacency_matrix_to_edge_list(adj_matrix, cities):
    edge_list = []
    for i in range(len(adj_matrix)):
        for j in range(i + 1, len(adj_matrix)): #Samo gornji trokut jer je simetricna
            edge_list.append((i, j, adj_matrix[i][j]))

    return edge_list

def main():
    path = '/Users/markozdilar/Faks/2023-2024/Graf Algoritmi/Vj6/distance copy.csv'
    cities, adj_matrix = csv_to_adj_matrix(path)
    
    #print(cities)
    print_list(adj_matrix)
    edges = adjacency_matrix_to_edge_list(adj_matrix, cities)
    print(edges)

    start = time.time()
    graph = sorted_neighbors_algorithm(edges, len(cities))
    end = time.time()
    print("Time of execution: " + str(end - start) + " seconds.")
    print(graph)
    
if __name__ == "__main__":
    main()