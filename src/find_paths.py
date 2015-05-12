# -*- coding: utf-8 -*-
#+Author:Allen Woods 
import copy

def find_all_paths(edges, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in edges:
            return []
        paths = []
        for node in edges[start]:
            if node not in path:
                newpaths = find_all_paths(edges, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_paths(path_list):
    shortest_paths = list()
    shortest_len = min([len(l) for l in path_list])
    for l in path_list:
        if len(l) == shortest_len:
            shortest_paths.append(l)
    return shortest_paths
    
def all_shortest_paths(graph):
    nodes = graph.nodes
    edges = graph.edges
    shortest_path = list()
    for node in nodes:
        other_nodes = copy.deepcopy(nodes)
        remove_list = list()
        for n in other_nodes:
            if n <= node:
                remove_list.append(n)
        for n in remove_list:
            other_nodes.remove(n)
        for other_n in other_nodes:
            p = find_all_paths(edges,node, other_n)
            sp = find_shortest_paths(p)
            shortest_path.append(sp)
    return(shortest_path)
