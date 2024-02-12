'''
Konačan, neusmjeren i povezan graf je Eulerov ako i samo ako su su svi vrhovi parnog stupnja

Ako je graf povezan i svaki vrh ima paran stupanj, onda imamo eulerov ciklus (vraca se u isti vrh)


Graf je Eulerov ako ima točno nula ili točno dva vrha čiji je stupanj neparan,
a svi ostali vrhovi imaju paran stupanj.

Ako su svi vrhovi grafa parnog stupnja, graf je Eulerov.
Ako su točno dva vrha neparnog stupnja, graf je Eulerov, i ti vrhovi su početni i završni vrh putanje.
Inače, graf nije Eulerov.
Ovo proizlazi iz Eulerovog teorema o postojanju Eulerovih puteva i ciklusa u grafu.

'''

from Vj4.zdilar_marko_4_1 import read_pajek, adjacency_matrix_from_graph_data

def is_eulerian(graph):
    degrees = []
    odd_degrees = 0

    for row in graph: #Napuniti stupnjeve grafa
        degree = sum(row)
        degrees.append(degree)

    for deg in degrees: #Ako nije paran, onda cemo trebati imati tocno 2 takva vrha
        if deg % 2 != 0:
            odd_degrees += 1

    #return odd_degrees == 0 or odd_degrees == 2
    return odd_degrees == 0

def main():
    file_name = 'euler.net'
    graph_data = read_pajek(file_name)
    adj_matrix = adjacency_matrix_from_graph_data(graph_data)
    if(is_eulerian(adj_matrix)):
        print("Graph is Euler's.")
    else:
        print("Graph is not Euler's.")


if __name__ == "__main__":
    main()