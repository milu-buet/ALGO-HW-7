#Author: Milu
from graph import DGraph
import random


def create_complete_weighted_undirected_graph(n, weight_limit):
    g = DGraph()
    for i in range(n):
        for j in range(i+1,n):
            #print (i,j)
            random_weight = random.randint(1,weight_limit)
            g.add(i,j,random_weight)
            g.add(j,i,random_weight)
    return g



def getMinTour(g,n,i,current_weight):
    global min_weight,min_path
    if promising(i,current_weight):
        if i == n-1:
            path[i+1] = path[0]
            if g[path[i],path[0]]:
                new_weight = current_weight + g[path[i],path[0]]
            else:
                new_weight = current_weight
            getMinTour(g,n,i+1,new_weight)
        elif i == n:
            min_weight = current_weight
            min_path = path[0:]
            print(path,current_weight)
        else:
            for j in range(n):
                if j not in path[0:i+1]:
                    path[i+1] = j
                    if g[path[i],j]:
                        new_weight = current_weight + g[path[i],j]
                    else:
                        new_weight = current_weight

                    getMinTour(g,n,i+1,new_weight)


def promising(i,current_weight):
    if min_weight is None or current_weight < min_weight:
        return True
    return False




n = 15
weight_limit = 100
g = create_complete_weighted_undirected_graph(n,weight_limit)
path = [None]*(n+1)
min_weight = None
min_path = None

# print(g.Vertices)
#print(g.Edges)

getMinTour(g,n,-1,0)
print(min_path,min_weight)
