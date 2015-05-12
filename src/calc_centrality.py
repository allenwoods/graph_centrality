# -*- coding: utf-8 -*-
#+Author:Allen Woods 

import numpy as np
import numpy.linalg as la
import src.find_paths as find
mat = np.matrix

def degree_centrality(graph):
    degree = [sum(line) for line in graph.adj_mtx]
    return degree
    
def eigenvector_centrality(graph):
    return la.eigvals(graph.adj_mtx)
    
def katz_centrality(graph, alpha=0.3, beta=0.3):
    A = graph.adj_mtx
    I = np.identity(len(A))
    one = np.array([1 for i in range(len(A))])
    katz = (beta*mat(I - alpha*A.T).I).dot(one)
    # Change into list for further process
    return katz.A1
    
def pagerank_centrality(graph):
    A = graph.adj_mtx
    I = np.identity(len(A))

    D = np.identity(len(A))
    count = 0
    for i in A.sum(axis=1):
        D[count] = np.multiply(D[count],i)
        count += 1
    D = np.mat(D)

    alpha = 1/max(la.eigvals(A)) * 0.9
    beta = 0.3
    one = np.array([1 for i in range(len(A))])
    pagerank = (beta*mat(I -mat((alpha*A.T).dot(D.I))).I.dot(one))
    return pagerank.A1
    
def betweenness_centrality(graph):
    shortest_paths = find.all_shortest_paths(graph)
    nodes = graph.nodes
    betweenness = list()
    for n in nodes:
        n_betweenness = 0
        for paths in shortest_paths:
            sub_n_betweenness = 0
            for path in paths:
                if n in path[1:-1]:  
                #Don't need the path has the node on both end
                    sub_n_betweenness += 1
            n_betweenness += (sub_n_betweenness/len(paths))*2
        betweenness.append(n_betweenness)
    return betweenness
    
def closeness_centrality(graph):
    shortest_paths = find.all_shortest_paths(graph)
    nodes = graph.nodes
    closeness = list()
    for n in nodes:
        n_closeness = 0
        for paths in shortest_paths:
            sub_n_closeness = 0
            for path in paths:
                if n not in path[:1] and n not in path[-1:]:
                    break
                else:
                    sub_n_closeness = len(path)-1
                    break
            n_closeness += sub_n_closeness
        closeness.append(1/(n_closeness/(len(nodes)-1)))
    return closeness
