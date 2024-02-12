def read_pajek(file_path):
    graph = {'vertices': [], 'arcs': []}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        section = None
        
        for line in lines:
            line = line.split()
            if(line[0] == "*vertices"):
                section = "vertices"
                continue
            elif(line[0] == "*arcs"):
                section = "arcs"
                continue

            if(section == "vertices"):
                vertex_id = int(line[0])
                vertex_label = ' '.join(line[1:]) #line nekad ima vise od 2 elementa (kada naziv grada ima vise rijeci)
                graph['vertices'].append([vertex_id, vertex_label[1:-1]]) #Removamo prvi i zadnji element stringa - Dupli navodnici
            if(section == "arcs"):
                graph['arcs'].append([int(line[0]), int(line[1])])

    return graph

def dfs(graph, start, visited, component):
    # DFS algoritam s manjim optimizacijama
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            component.add(vertex)
            neighbors = set()
            for edge in graph:
                if edge[0] == vertex:
                    neighbors.add(edge[1])
            stack.extend(neighbors)

def find_components(graph):
    # Pronalaženje svih komponenti u grafu
    visited = set()
    components = []
    for vertex in graph['vertices']:
        vertex_id = vertex[0]
        if vertex_id not in visited:
            component = set()
            dfs(graph['arcs'], vertex_id, visited, component)
            components.append(component)
    return components

def main():
    file_path = 'C:\\Users\\mzdil\\Desktop\\Faks\\2023-2024\\Graf_Algoritmi\\Vj5\\eva.net'
    graph = read_pajek(file_path)

    components = find_components(graph)
    #Komponenta - Skup cvorova koji su međusobno povezani putem bridova, tj. moze se iz jednog doc u drugi nekim putem
    #Npr - u povezanom grafu, imamo samo 1 komponentu
    print(f"Broj komponenti u grafu: {len(components)}")

    largest_component = max(components, key=len) #Clan sa najvise elemenata
    print(f"Veličina najveće komponente: {len(largest_component)}")

    # Sortiranje komponenti prema veličini u padajućem redoslijedu
    sorted_components = sorted(components, key=len, reverse=True)
    vertex_dict = {vertex[0]: vertex[1] for vertex in graph['vertices']}
    for i, component in enumerate(sorted_components[:10], 1): #Prvih 10 jer je padajuća, počevši od 1
        representative_vertex = component.pop()
        vertex_label = vertex_dict[representative_vertex]
        print(f"{i}. {vertex_label}: {len(component)}")
        component.add(representative_vertex) #Samo ga vracamo nazad

if __name__ == "__main__":
    main()
