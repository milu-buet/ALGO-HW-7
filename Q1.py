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



def getMinTour(g,n,i):
    global min_weight,min_path,path
    current_weight = get_path_weight(g,i,path)
    if promising(i,current_weight):
        if i == n:
            min_weight = current_weight
            min_path = path[0:]
            #print(path,current_weight)
        elif i == n-1:
            path[i+1] = path[0]
            getMinTour(g,n,i+1)
        else:
            for j in range(n):
                if j not in path[0:i+1]:
                    path[i+1] = j
                    getMinTour(g,n,i+1)


def get_path_weight(g,j,path):
	total_weight = 0
	for i in range(j):
		if g[path[i],path[i+1]]:
			total_weight+=g[path[i],path[i+1]]
		else:
			print(g.Edges,path[i],path[i+1])
	return total_weight

def promising(i,current_weight):

    # #print(min_path)
    if min_weight is None or current_weight < min_weight:
        return True
    return False




for i in range(3,10):
    n = i
    weight_limit = 10
    g = create_complete_weighted_undirected_graph(n,weight_limit)
    path = [None]*(n+1)
    min_weight = None
    min_path = None

    # print(g.Vertices)
    #print(g.Edges)

    getMinTour(g,n,-1)
    print(n,min_path,min_weight)
