#Author: Milu
from graph import DGraph
import random


def create_complete_weighted_undirected_graph(n, weight_limit):
    g = DGraph()
    for i in range(n):
        for j in range(i+1,n):
            random_weight = random.randint(1,weight_limit)
            g.add(i,j,random_weight)
            g.add(j,i,random_weight)
    return g

def getMinTour(g,n,i):
    global min_weight,min_tour,config
    current_weight = get_tour_weight(g,i,config)
    if promising(i,current_weight,min_weight):
        if i == n-1:
            min_weight = current_weight
            min_tour = config[0:] + [config[0]]
        else:
            for j in range(n):
                if j not in config[0:i+1]:
                    config[i+1] = j
                    getMinTour(g,n,i+1)


def get_tour_weight(g,j,config):
    if j <= 0:
        return None
    total_weight = 0
    for i in range(j):
        total_weight+=g[config[i],config[i+1]]
    total_weight+= g[config[j],config[0]]
    return total_weight

def promising(i,current_weight,min_weight):
    if min_weight is None or current_weight < min_weight:
        return True
    return False

for i in range(3,12):
    n = i
    weight_limit = 10
    g = create_complete_weighted_undirected_graph(n,weight_limit)
    config = [None]*(n)
    min_weight = None
    min_tour = None
    getMinTour(g,n,-1)
    print(n,min_tour,min_weight)
