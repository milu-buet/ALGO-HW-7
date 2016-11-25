#Author: Milu
from graph import DGraph
import random


def create_complete_weighted_undirected_graph(n, weight_limit):
    g = DGraph()
    for i in range(n):
        for j in range(i,n):
            random_weight = random.randint(0,weight_limit)
            g.add(i,j,random_weight)
            g.add(j,i,random_weight)
    return g


g = create_complete_weighted_undirected_graph(5,100)
print(g.__dict__)
