from os import path


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
    if(destino in root.children_array()):
        path_so_far.append(destino)
        paths.append(path_so_far)
        return
    else:
        for child in root.children:
            get_path_util(child,destino,path_so_far.copy())