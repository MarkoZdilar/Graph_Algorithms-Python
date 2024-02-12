from Vj4.zdilar_marko_4_1 import read_pajek, adjacency_matrix_from_graph_data


def count_vertices(adj_matrix):
    return len(adj_matrix)

def count_edges(adj_matrix):
    total_edges = 0
    for row in adj_matrix:
        total_edges += sum(row)
    
    return total_edges // 2

def degree_of_vertex(adjacency_matrix, vertex):
    return sum(adjacency_matrix[vertex - 1]) #zbrojimo jedinice u tom redu, tj. broj drugih vrhova sa kojima je taj vrh povezan

def max_degrees(degrees):
    max_degree_list = []
    max_degree_value = 0
    for degree_name, degree_value in degrees.items(): #Nadjemo najveci degree
        if(max_degree_value < degree_value):
            max_degree_value = degree_value

    for degree_name, degree_value in degrees.items(): #Usporedjivamo sve sa najvecim
        if(max_degree_value <= degree_value):
            max_degree_list.append([degree_name, degree_value])

    return max_degree_list


def main():
    file_name = 'euler.net'
    graph_data = read_pajek(file_name)
    adj_matrix = adjacency_matrix_from_graph_data(graph_data)

    # ----- 1 -----
    print(f"Number of vertices: {count_vertices(adj_matrix)}")

    # ----- 2 -----
    print(f"Number of edges: {count_edges(adj_matrix)}")

    # ----- 3 -----
    print("Vertices degrees:")
    degrees = {}
    for vertex_id, vertex_name in graph_data['vertices'].items():
        degree = degree_of_vertex(adj_matrix, vertex_id)
        degrees[vertex_name] = degree
        print(f"{vertex_name}: {degree}")

    # ----- 4 -----
    print("Vertices with max degrees:")
    for degree in max_degrees(degrees):
        print(f"{degree[0]} with degree of {degree[1]}")


if __name__ == "__main__":
    main()