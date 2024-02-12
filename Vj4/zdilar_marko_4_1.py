import os
'''
Teorija
Vertices - Vrhovi
Arcs - Usmjereni bridovi (imaju tezinu brida)
Edges - Neusmjereni bridovi

Vertice:
 | 1 "ARG" |  -> vrh 1, oznaka mu je ARG
Arc:
 | 1 12 4 | -> Usmjereni brid koji ide od vrha 1 do vrha 12, a tezina mu je 4
Edge:
 | 1 2 | -> Neusmjereni brid koji ide od vrha 1 do vrha 2

Arcs i Edges su oboje bridovi, samo sto Arcs imaju definiranu tezinu
Brid je incidentan s vrhovima koji su njegovi krajevi
Stupanj vrha je broj bridova incidentnih s njim

matrica susjedstva - ako vrh ide iz 1 u 12, a tezina mu je 4, onda u matrici na mjestima (1,12) i (12,1) imamo vrijedost 4
matrica incidencije - retci u matrici su vrhovi | stupci su bridovi -> Vrhovi koji su spojeni imaju 1, ostali 0. Zbroj svakog stupca mora biti 2.
lista susjedstva grafa - 


'''
def read_pajek(file_name):
    script_dir = os.path.dirname(__file__)  # path do .py
    file_path = os.path.join(script_dir, file_name)
    graph_data = {'vertices': {}, 'edges': []} #
    currentPart = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.split()
            if(len(line) == 0):
                continue
            if line[0] == '*Vertices':
                currentPart = 'vertices'
            elif line[0] == '*Arcs':
                currentPart = 'arcs'
            elif line[0] == '*Edges':
                currentPart = 'edges'
            elif currentPart == 'vertices' and len(line) != 0:
                id = int(line[0])
                vertex_label = line[1].strip('"')
                graph_data['vertices'][id] = vertex_label
            elif currentPart == 'arcs' and len(line) != 0:
                firstEdge = int(line[0])
                secondEdge = int(line[1])
                weight = int(line[2])
                graph_data['edges'].append({'firstEdge': firstEdge, 'secondEdge': secondEdge, 'weight': weight})
            elif currentPart == 'edges':
                firstEdge = int(line[0])
                secondEdge = int(line[1])
                graph_data['edges'].append({'firstEdge': firstEdge, 'secondEdge': secondEdge})

    return graph_data

def adjacency_matrix_from_graph_data(graph_data):
    num_vertices = len(graph_data['vertices'])
    matrix = []
    for _ in range(num_vertices): #punimo matricu nulama
        row = [0] * num_vertices
        matrix.append(row)

    for edge in graph_data['edges']:
        if("weight" in edge):
            firstEdge, secondEdge, weight = edge['firstEdge'], edge['secondEdge'], edge['weight']
            matrix[firstEdge - 1][secondEdge - 1] = weight
            matrix[secondEdge - 1][firstEdge - 1] = weight
        else:
            firstEdge, secondEdge = edge['firstEdge'], edge['secondEdge']
            matrix[firstEdge - 1][secondEdge - 1] = 1
            matrix[secondEdge - 1][firstEdge - 1] = 1

    return matrix

def incidence_matrix_from_adjacency(adjacency_matrix):
    num_vertices = len(adjacency_matrix) #Duzina liste listi - broj vrhova
    total_edges = 0
    for row in adjacency_matrix:
        total_edges += sum(row)

    num_edges = total_edges // 2  #Svaki cemo brid imati zabiljezen 2 puta u matrici susjedstva (1,4) (4,1)

    incidence_matrix = []
    for _ in range(num_vertices): #Napunimo matricu nulama | broj redaka = broj vrhova, broj stupaca = broj bridova
        incidence_matrix.append([0] * num_edges)

    #i=redak, j=stupac
    column_index = 0
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            # Prolazimo samo gornji trokut matrice - donji nema smisla jer je isti (neusmjeren graf)
            #i + 1 jer na glavnoj dijagonali imamo 0 (vrh ne moze bridom biti povezan sobom)
            if adjacency_matrix[i][j] == 1:
                incidence_matrix[i][column_index] = 1
                incidence_matrix[j][column_index] = 1
                #Kada u istom stupcu setiramo 2 vrha u 1, idemo na iduci stupac.
                column_index += 1

    return incidence_matrix

def adjacency_matrix_from_incidence(incidence_matrix):
    num_vertices = len(incidence_matrix)
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for j in range(len(incidence_matrix[0])):  # Prolazak kroz stupce
        vertices = []
        for i in range(num_vertices):  # Prolazak kroz retke
            if incidence_matrix[i][j] == 1:
                vertices.append(i)
        if len(vertices) == 2:  # Ako su točno dva vrha povezana bridom idu jedinice
            adjacency_matrix[vertices[0]][vertices[1]] = 1
            adjacency_matrix[vertices[1]][vertices[0]] = 1

    return adjacency_matrix

def adjacency_list_from_adjacency_matrix(adjacency_matrix, vertex_labels):
    num_vertices = len(adjacency_matrix)
    adjacency_list = {}

    for i in range(num_vertices):
        neighbors = []
        for j in range(num_vertices):
            if adjacency_matrix[i][j] == 1:
                neighbors.append(vertex_labels[j])
        adjacency_list[vertex_labels[i]] = neighbors

    return adjacency_list

def adjacency_list_from_incidence(incidence_matrix, vertex_labels):
    num_vertices = len(incidence_matrix)
    adjacency_list = {label: [] for label in vertex_labels}

    for j in range(len(incidence_matrix[0])):  # Prolazak kroz stupce
        vertices = []
        for i in range(num_vertices):  # Prolazak kroz retke
            if incidence_matrix[i][j] == 1:
                vertices.append(vertex_labels[i])
        if len(vertices) == 2:  # Ako su točno dva vrha povezana bridom
            adjacency_list[vertices[0]].append(vertices[1])
            adjacency_list[vertices[1]].append(vertices[0])

    return adjacency_list

def adjacency_matrix_from_list(adjacency_list):
    num_vertices = len(adjacency_list)
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    label_to_index = {label: i for i, label in enumerate(adjacency_list.keys())}

    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            i, j = label_to_index[vertex], label_to_index[neighbor]
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1

    return adjacency_matrix

def incidence_matrix_from_list(adjacency_list):
    num_vertices = len(adjacency_list)
    edges = set()
    label_to_index = {label: i for i, label in enumerate(adjacency_list.keys())}

    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            edge = tuple(sorted([vertex, neighbor]))
            edges.add(edge)

    num_edges = len(edges)
    incidence_matrix = [[0 for _ in range(num_edges)] for _ in range(num_vertices)]
    edge_to_column = {edge: i for i, edge in enumerate(edges)}

    for edge, column in edge_to_column.items():
        v1, v2 = edge
        i, j = label_to_index[v1], label_to_index[v2]
        incidence_matrix[i][column] = 1
        incidence_matrix[j][column] = 1

    return incidence_matrix

def print_matrix(name, matrix):
    print(f"{name} matrix")
    for row in matrix:
        print(row)
    print('\n')

def main():
    file_name = 'euler.net'
    graph_data = read_pajek(file_name)

    adj_matrix = adjacency_matrix_from_graph_data(graph_data)

    inc_matrix = incidence_matrix_from_adjacency(adj_matrix)
    adj_matrix2 = adjacency_matrix_from_incidence(inc_matrix)

    #Nadjemo slovne oznake vrhova, kako bi ih mogli kasnije tako i ispisati
    vertex_labels = list(graph_data['vertices'].values())
    adj_list = adjacency_list_from_adjacency_matrix(adj_matrix, vertex_labels)
    adj_list2 = adjacency_list_from_incidence(inc_matrix, vertex_labels)

    adj_matrix3 = adjacency_matrix_from_list(adj_list)
    inc_matrix2 = incidence_matrix_from_list(adj_list)

    print_matrix("Adjacency", adj_matrix)
    print_matrix("Adjacency 2", adj_matrix2)
    print_matrix("Adjacency 3", adj_matrix3)
    print_matrix("Incidence", inc_matrix)
    print_matrix("Incidence 2", inc_matrix2)
    print("Adjacency list of a graph")
    for vertex, list_neighbors in adj_list.items():
        print(f"{vertex}: {list_neighbors}")
    print("Adjacency list 2 of a graph")
    for vertex, list_neighbors in adj_list2.items():
        print(f"{vertex}: {list_neighbors}")

if __name__ == "__main__":
    main()