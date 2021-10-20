


def hi():
    print("Hello")

total_paths = []
def get_total_paths(root):
    path_so_far=[]
    get_total_paths_util(root,path_so_far)
    return total_paths

def get_total_paths_util(root,path_so_far):
    global total_paths
    path_so_far.append(root.data)
    total_paths.append(path_so_far)
    for child in root.children:
        get_total_paths_util(child, path_so_far.copy())


NodosTerminales = []
def find_end_nodes(root): 
    global NodosTerminales
    if(root.children == []):
        NodosTerminales.append(root.data)
    else:
        for child in root.children:
                find_end_nodes(child)

    return len(NodosTerminales)

paths = []
def get_path(root,destino):
    global paths
    path_so_far = []
    get_path_util(root,destino,path_so_far)
    return paths

def get_path_util(root,destino,path_so_far):
    global paths
    path_so_far.append(root.data)

    for child in root.children:
        if(destino == child.data):
            new_path_so_far = path_so_far.copy()
            new_path_so_far.append(destino)
            paths.append(new_path_so_far)
        else:
            get_path_util(child,destino,path_so_far.copy())

total_edges = 0
def get_edges(root):
    global total_edges
    for child in root.children:
        total_edges+=1
        get_edges(child)
    
    return total_edges

acyclic_nodes = 0
def find_cycles(root):
    global acyclic_nodes
    acyclic_nodes += len(root.children_array()) - len(set(root.children_array()))

    for child in root.children:
        find_cycles(child)
    return acyclic_nodes

    




