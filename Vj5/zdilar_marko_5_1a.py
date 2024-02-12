import heapq
import random

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
                graph['vertices'].append([int(line[0]), line[1]])
            if(section == "arcs"):
                graph['arcs'].append([int(line[0]), int(line[1]), int(line[2])])

    return graph

def prim(graph):
    randomVertex = random.randint(0, len(graph['vertices']) - 1)
    start_vertex = graph['vertices'][randomVertex][0] #Uzimamo uvijek random vrh kao prvi - MST mora biti isti
    min_heap = [(0, start_vertex, None)]  # 0 - udaljenost - tezina (Prvi cvor je udaljen od sebe 0) | ID cvora | prethodni cvor

    visited = []
    min_spanning_tree = []

    while min_heap:
        #Weight obavezno na prvom mjestu, jer se elementi na heap-u sortiraju prema njemu.
        #Sto znaci, da kada radimo heappop(uzimamo najgornjeg - najmanji weight za taj brid)
        weight, current_vertex, parent = heapq.heappop(min_heap)

        #Ako smo posjetili cvor, preskacemo -> Osiguravamo da se ne vracamo u isti (da ne radimo ciklus)
        if current_vertex not in visited:
            visited.append(current_vertex)

            #Ako nije pocetni cvor - brid dodajemo u MST
            #Jer u slucaju prvog cvora, ne znamo jos koje moguce bridove imamo.
            if parent is not None:
                min_spanning_tree.append([parent, current_vertex, weight])

            #Provjeravano sve bridove koji su povezani sa trenutnim cvorom i dodajemo ga na heap
            #Primjer cvora [1,2,343] -> [od, do, tezina]
            for edge in graph['arcs']:
                if edge[0] == current_vertex and edge[1] not in visited: # Ako je PRVI kraj brida nas cvor
                    heapq.heappush(min_heap, (edge[2], edge[1], current_vertex)) #u min_heap dodajemo brid
                elif edge[1] == current_vertex and edge[0] not in visited: # Ako je DRUGI kraj brida nas cvor
                    heapq.heappush(min_heap, (edge[2], edge[0], current_vertex)) #u min_heap dodajemo brid

    return min_spanning_tree

def print_mst(mst, vertex_names):
    print("Minimalno razapinjuće stablo:")
    for edge in mst:
        start, end, weight = edge
        start_name = vertex_names[start][1]
        end_name = vertex_names[end][1]
        print(f"{start_name} - {end_name} -> {weight}")

def main():
    filePath = 'C:\\Users\\mzdil\\Desktop\\Faks\\2023-2024\\Graf_Algoritmi\\Vj5\\airports-split-modified.net'
    data = read_pajek(filePath)
    mst = prim(data)
    print_mst(mst, data['vertices']) #Saljemo data['vertices'] radi imena bridova

if __name__ == "__main__":
    main()
