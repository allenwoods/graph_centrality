# -*- coding: utf-8 -*-
#+Author:Allen Woods 

from src.structure import graph, select_top
import src.calc_centrality as calc
from prettytable import PrettyTable

def print_table(graph, centrality_method, centrality):
    table = PrettyTable(["No.", "Vertex", centrality])
    table.align["No."] = "c"
    cen_results = centrality_method(graph)
    #cen_list = zip(graph.nodes, cen_results)
    seq = select_top(cen_results, len(cen_results))
    i = 1
    for item in seq:    
        table.add_row([str(i),"v"+str(item),str(cen_results[item-1])])
        i += 1
    print(table)

def mission():
    print_table(graph_1, calc.degree_centrality, "Degree Centrality")
    print_table(graph_1, calc.eigenvector_centrality, "Eigenvector Centrality")
    print_table(graph_1, calc.katz_centrality, "Katz Centrality")
    print_table(graph_1, calc.pagerank_centrality, "PageRank Centrality")
    print_table(graph_1, calc.betweenness_centrality, "Betweenness Centrality")
    print_table(graph_1, calc.closeness_centrality, "Closeness Centrality")
    



if __name__ == '__main__':
    test_edges_1 = [[1,2],[2,3],[3,4],[3,5],[3,6],[4,5],[4,6],[5,6],[6,7],[7,8],[7,9],[8,9],[8,10],[9,10]]
    graph_1 = graph(0,test_edges_1)
    test_edges_2 = [[1,2],[2,3],[3,5],[2,4],[4,5]]
    graph_2 = graph(1,test_edges_2)
    mission()

    
