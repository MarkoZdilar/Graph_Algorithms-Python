from operator import itemgetter
from zdilar_marko_5_1a import print_mst, read_pajek

def sort_graph(graph_data):
    sorted_graph = {'vertices': graph_data['vertices'], 'arcs': sorted(graph_data['arcs'], key=itemgetter(2))}
    return sorted_graph

def find_set(sets, vertex):
    for key, value in sets.items():
        if vertex in value: #Ako su start i end vec u istom setu, vratit ce se isti key od tog seta
            return key

def union_sets(sets, set1, set2):
    sets[set1] |= sets[set2]
    del sets[set2]

def kruskal(graph):
    graph = sort_graph(graph)
    min_spanning_tree = []

    #Napravimo nove setove
    #Na pocetku svaki vrh ima samo sebe, tj { 0: {0}, 1: {1}...}
    #Na pocetku onoliko setova koliko vrhova
    #Zato jer nijedan brid nije spojen - Kada se spoji, doda se setu sa kojim je spojen, i taj se set izbrise da se ne ponovi
    #Kada ostane samo 1 set, imamo MST - Povezali smo sve
    sets = {}
    for vertex in graph['vertices']: 
        vertex_id = vertex[0]
        sets[vertex_id] = {vertex_id}

    #Proc cemo po svim bridovima (Ovdje su vec sortirani)
    for edge in graph['arcs']:
        if(len(min_spanning_tree) == len(graph['vertices']) - 1):
            break
        start = edge[0]
        end = edge[1]

        set_start = find_set(sets, start)
        set_end = find_set(sets, end)

        if set_start != set_end: #Ako su isti (znaci vec su u istom setu) - stvaramo ciklus i ne dodajemo ga u MST
            min_spanning_tree.append(edge)
            union_sets(sets, set_start, set_end)

    return min_spanning_tree

def main():
    filePath = 'C:\\Users\\mzdil\\Desktop\\Faks\\2023-2024\\Graf_Algoritmi\\Vj5\\airports-split-modified.net' # Modified primjer slijedi slajdove
    data = read_pajek(filePath)
    mst = kruskal(data)
    print_mst(mst, data['vertices'])

if __name__ == "__main__":
    main()