from dataDB import generarBD
from GraphFunc import *
from AnwerTools import *

# Data
data = generarBD()
unique_data = get_unique_dest(data)


# Graphs
graph = create_graph(data, unique_data)
visit = set()
tree = create_tree(graph, "Tecnologico", visit)


# Driver Code
#visited = set()
# dfs(visited,graph,"Tecnologico")
#tree.children[0].print_children()


# RESPUESTAS
print("1)\n"+str(len(unique_data)) + " Nodos totales")
print(str(get_edges(tree))+ " Viajes totales")
print(str(len(unique_data)-find_cycles(tree)) + " Nodos aciclicos")

print("2) Hay " + str(find_end_nodes(tree)) + " Nodos Terminales")

caminos = get_path(tree,'Rincon colonial')
print("3) Primer solucion: "+ str(caminos[0])) #Rincon colonial
print("4) Tercera solucion: "+ str(caminos[2]))
print("5) Quinta solucion: "+ str(caminos[4]))
print("6) Ultima solucion: "+ str(caminos[-1]))

