from dataDB import generarBD
from GraphFunc import *

#Data
data = generarBD()
unique_data=get_unique_dest(data)
graph = create_graph(data,unique_data)


#Logic
visited = set()
visit=set()
#dfs(visited,graph,"Tecnologico")
tree = create_tree(graph,"Tecnologico",visit)
tree.print_children()

# Driver Code
#dfs(visited, graph, "A")

#RESPUESTAS
#print("1) "+str(len(unique_data)) + " Nodos totales")