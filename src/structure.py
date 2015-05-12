# -*- coding: utf-8 -*-
#+Author: Allen Woods
import numpy as np
import copy

class graph():
    def __init__(self, graph_ID, edges_list=[], is_undirected = True):
        self.ID = graph_ID
        self.is_undirected = is_undirected
        self.nodes = list()
        self.edges = dict()
        self.add_edge(edges_list)
        self.adj_mtx = self.gen_adjmtx()
        
    def update_node_list(self):
        self.nodes.extend(self.edges.keys())
            
    def add_edge(self, edges_list):
        for edge in edges_list:
            if edge[0] not in self.edges.keys():
                self.edges[edge[0]] = list()
            if edge[1] not in self.edges.keys():
                self.edges[edge[1]] = list()
            self.edges[edge[0]].append(edge[1])
            if self.is_undirected:
                self.edges[edge[1]].append(edge[0])
        self.update_node_list()
        self.adj_mtx = self.gen_adjmtx()
        
    def gen_adjmtx(self):
        length = len(self.nodes)
        adjmtx = [[0 for n in range(length)] for n in range(length)]
        for i in self.nodes:
            for j in self.edges[i]:
                adjmtx[i-1][j-1] = 1
        return np.array(adjmtx)

    
def select_top(results, num):
    seq = list()
    lis = copy.deepcopy(results)
    if num > len(lis)+1:
        return "Wrong Number! More than items in the list"
    while len(seq) < num:
        i = 0
        for i in range(len(lis)):
            max_num = max(lis)
            if lis[i] == max_num:
                seq.append(i+1)
                lis[i] = -1
                if len(seq) >= num:
                    break
    return seq
    
