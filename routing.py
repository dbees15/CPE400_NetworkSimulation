import networkx as nx
import random

MINNUM = 0

#==========Search Functions and Helpers==========

#Private method _breadthfirstsearch
#returns list indicating shortest path distance from node start_index to all other nodes
#Parameters:
#   graph: networkx graph object
#   start_index: the starting node index
def _breadthfirstsearch(gr: nx.Graph,start_index):    #return shortest path list for all nodes
    shortest_path_list = []
    for n in range(0,gr.number_of_nodes()):
        path = nx.shortest_path(gr,source=start_index,target=n)
        shortest_path_list.append(len(path))
    return shortest_path_list

#Private method _heuristicgraph
#Returns a new graph object with powers equal to their heuristic relative to the source and target
#Parameters:
#   graph: networkx graph object
#   start_index: the starting node index
#   target_index: target node index
def _heuristicgraph(graph : nx.Graph,source_index,destination_index):
    new_graph = nx.Graph(graph)
    for i in range(0,graph.number_of_nodes()):
        distance = _breadthfirstsearch(graph,destination_index)[i]
        #print(f"{i}: "+str(distance))
        if graph.nodes[i]['power'] != 0:
            new_graph.nodes[i]['power'] = 1/(graph.nodes[i]['power'] / distance)
        else:
            new_graph.nodes[i]['power'] = float('inf')
    return new_graph

#Public method bestpath
#Returns a list of node indexes of the best path from start node to target node
#Parameters:
#   graph: networkx graph object
#   start_index: the starting node index
#   target_index: target node index
def bestpath(graph: nx.Graph,start_index : int,target_index : int):
    h = _heuristicgraph(graph,start_index,target_index)
    def heuristic(a,b,G=h):
        return (G.nodes[a]['power'])
    path = nx.astar_path(h,start_index,target_index,heuristic)
    return path

#==========Graph Generation and Simulation Functions==========

#generate graph with 8 nodes with random powers in range 100 to maxpower
#Parameters:
#   maxpower: int : max power a node can have
#maxpower should be multiple of 100 - such as 1000,1100,2000
def generate_graph_8(maxpower : int):
    maxpower/=100
    g = nx.Graph()
    for x in range(0,8):
        g.add_node(x,power=(random.randint(1,maxpower))*100)
    #add edges
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,5)
    g.add_edge(3,6)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(4,6)
    g.add_edge(5,6)
    g.add_edge(5,7)
    g.add_edge(6,7)
    return g

def generate_graph_10(maxpower : int):
    maxpower/=100
    g = nx.Graph()
    for x in range(0,10):
        g.add_node(x,power=(random.randint(1,maxpower))*100)
    #add edges
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,5)
    g.add_edge(3,6)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(4,6)
    g.add_edge(5,6)
    g.add_edge(5,7)
    g.add_edge(5,8)
    g.add_edge(6,7)
    g.add_edge(6,8)
    g.add_edge(7,9)
    g.add_edge(7,8)
    g.add_edge(8,9)
    return g

def generate_graph_6(maxpower : int):
    maxpower/=100
    g = nx.Graph()
    for x in range(0,6):
        g.add_node(x,power=(random.randint(1,maxpower))*100)
    #add edges
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,5)
    g.add_edge(3,4)
    g.add_edge(4,5)
    return g

#Public method simulate
#Returns number of packets were able to be transmitted from source index of a random generated graph, to destination
#Parameters:
#   graph generator: function : function to generate a graph
#   maxpower: int : max power a node can have
#   reroute: bool : whether the simulation will try to reroute when a path is exhausted
#   source_index: int : the starting node index
#   destination_index: int : target node index
#   transmission cost: int : amount of power to reduce a node by per transmission

def simulate(graph_generator, maxpower, reroute : bool,source_index,destination_index,transmission_cost):
    g = graph_generator(maxpower)
    def _can_transmit(path):
        for i in path:
            if g.nodes[i]['power'] - transmission_cost < 0:
                return False
        return True

    def _remove_dead():
        for i in range(0,g.number_of_nodes()):
            if g.nodes[i]['power'] <=0 :
                g.nodes[i]['power'] = MINNUM

    def _no_path(path):
        for n in path:
            if g.nodes[n]['power'] == MINNUM:
                return True
        return False

    rerouted_num = 0
    packets_sent = 0
    best = bestpath(g,source_index,destination_index)
    while True:
        while _can_transmit(best):
            for n in range(0,len(best)-1):
                g.nodes[best[n]]['power'] -= transmission_cost
            packets_sent+=1
        _remove_dead()
        best = bestpath(g,source_index,destination_index)
        if not reroute:
            break
        if _no_path(best):
            break
        rerouted_num += 1
    return packets_sent,rerouted_num
