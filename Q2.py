#Author: Milu
from graph import DGraph
import random

def create_random_weighted_graph(n, weight_limit):
    g = DGraph()
    for i in range(n):
        for j in range(i+1,n):
            if random.randint(0,5) > 1:    #5/7 chance of connectivity
                random_weight = random.randint(1,weight_limit)
                g.add(i,j,random_weight)
                g.add(j,i,random_weight)
    return g


def getVertexCover(g,n,i):
    global config,min_config
    if promising(g,i):
        if i == n-1:
            if isValidCover(g,i,config):
                min_config = getConfigSet(g,config)
                #print(min_config)
        else:
            config[i+1] = False
            getVertexCover(g,n,i+1)

            config[i+1] = True
            getVertexCover(g,n,i+1)


def promising(g,i):
    count = 0
    for j in range(i+1):
        if config[j]:
            count +=1
    if min_config is None or count < len(min_config):
        #print(count,min_config)
        return True
    return False

def isValidCover(g,i,aconfig):
    covered_edges = {}
    for j in range(i+1):
        if config[j]:
            for k in g.Out[j]:
                covered_edges[j,k] = 1
                covered_edges[k,j] = 1

    if len(covered_edges.keys()) == len(g.Edges):
        return True

    return  False

def getConfigSet(g,config):
    config_set = []
    for i in range(len(config)):
        if config[i]:
            config_set.append(i)

    return config_set



for i in range(3,18):
    n = i
    weight_limit = 100
    g = create_random_weighted_graph(n,weight_limit)

    config = [None]*n
    min_config = None
    getVertexCover(g,n,-1)
    print(i,min_config)




