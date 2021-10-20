class treeNode:
    def __init__(self, data):
        self.children = []
        self.data = data

    def add_child(self, obj):
        self.children.append(obj)

    def print_children(self):
        [print(x.data) for x in self.children]
    
    def children_array(self):
        return [x.data for x in self.children]

    def get_children_length(self):
        return len(self.children)


# Titulos de los datos
ORIGEN = 0
DESTINO = 1
COSTO = 2
DISTANCIA = 3

visited = set()  # Set to keep track of visited nodes.
visit = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def create_tree(graph, root, visit):
    auxNode = treeNode(root)
    visit.add(root)
    for dest in graph[root]:
        if(dest not in visit):
            auxNode.add_child(create_tree(graph, dest, visit.copy()))
    return auxNode


def get_unique_dest(data):
    unique = set()
    for row in data:
        unique.add(row[ORIGEN])
        unique.add(row[DESTINO])

    return unique


def create_graph(data, unique_data):
    # "Key": [Data,Data]
    graph = {}
    for start in unique_data:
        destinations = [row[DESTINO] for row in data if (row[ORIGEN] == start)]
        graph[start] = destinations

    return graph
