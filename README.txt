
*****************************************************************
REQUIREMENTS AND EXECUTION:
*****************************************************************

Requires Python3 and module NetworkX
Install networkx with command:
	pip install networkx

Run the demo with command: python3 demo.py

*****************************************************************
DOCUMENTATION:
*****************************************************************

=========================================
Routing.py:
=========================================

Purpose: Provide functions used to build the simulation demo

Functions:

Function _breadthfirstsearch
returns list indicating shortest path distance from node start_index to all other nodes
Parameters:
   graph: networkx graph object
   start_index: the starting node index

Function _heuristicgraph
Returns a new graph object with powers equal to their heuristic relative to the source and target
Parameters:
   graph: networkx graph object
   start_index: the starting node index
   target_index: target node index

Function bestpath
Returns a list of node indexes of the best path from start node to target node
Parameters:
   graph: networkx graph object
   start_index: the starting node index
   target_index: target node index

Function generate_graph_6
generate graph with 6 nodes with random powers in range 100 to maxpower
Parameters:
   maxpower: int : max power a node can have
maxpower should be multiple of 100 - such as 1000,1100,2000

Function generate_graph_8
generate graph with 8 nodes with random powers in range 100 to maxpower
Parameters:
   maxpower: int : max power a node can have
maxpower should be multiple of 100 - such as 1000,1100,2000

Function generate_graph_10
generate graph with 10 nodes with random powers in range 100 to maxpower
Parameters:
   maxpower: int : max power a node can have
maxpower should be multiple of 100 - such as 1000,1100,2000

Function generate_graph_12
generate graph with 12 nodes with random powers in range 100 to maxpower
Parameters:
   maxpower: int : max power a node can have
maxpower should be multiple of 100 - such as 1000,1100,2000

Function simulate
Returns number of packets were able to be transmitted from source index of a random generated graph, to destination
   also returns total number of reroutes performed
Parameters:
   graph generator: function : function to generate a graph
   maxpower: int : max power a node can have
   reroute: bool : whether the simulation will try to reroute when a path is exhausted
   source_index: int : the starting node index
   destination_index: int : target node index
   transmission cost: int : amount of power to reduce a node by per transmission


=========================================
demo.py:
=========================================

Purpose: Run several simulations to determine the effectiveness of the routing protocol

Functions:

Function tests
Runs simulation a number of times and prints the average of the simulation results with rerouting enabled and disabled
Parameters:
   graph_generator: function : function of what graph should be used for simulation
   targetnode: int : index of target node
   nodenum: int : number of nodes in graph, should correspond to graph_generator
   max_power: int : max power a node can have
   sim_num: int : number of times to run simulation
