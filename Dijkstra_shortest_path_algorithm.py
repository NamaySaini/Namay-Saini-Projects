import sys
from heapq import heapify, heappush, heappop

class ComputingNode:
    def __init__(self, cpu_cores, link_bandwidth, max_containers):
        self.cpu_cores = cpu_cores
        self.link_bandwidth = link_bandwidth
        self.max_containers = max_containers

    def get_cpu_cores(self):
        return self.cpu_cores

    def set_cpu_cores(self, cpu_cores):
        self.cpu_cores = cpu_cores

    def get_link_bandwidth(self):
        return self.link_bandwidth

    def set_link_bandwidth(self, link_bandwidth):
        self.link_bandwidth = link_bandwidth

    def get_max_containers(self):
        return self.max_containers

    def set_max_containers(self, max_containers):
        self.max_containers = max_containers

node = ComputingNode(cpu_cores=8, link_bandwidth=1000, max_containers=10)

def shortest(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]},
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(5): #the number of vertices of the path
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))

        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shorest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
    path = node_data[dest]['pred'] + list(dest)
    for i in range(0,len(path)-1):
        del(graph[str(path[i])][str(path[i+1])])
        

if __name__ == "__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
    }
    source = 'A'
    destination = 'F'
    shortest(graph,source,destination)

    
    