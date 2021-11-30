import networkx as nx
import random

MINNUM = float('-inf')

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
        new_graph.nodes[i]['power'] = 1/(graph.nodes[i]['power'] / distance)
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

#==========Graph Generation Functions==========

#generate graph with 8 nodes with random powers in range 100 to maxpower
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
