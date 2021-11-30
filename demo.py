import networkx
import routing
import random


#==========Script Body==========

print(f"8 node graph with node powers:")
g = routing.generate_graph_8(1000)

for i in range(g.number_of_nodes()):
    print(f"{i} - {g.nodes[i]}")
print("======")

print("best path from node 0 to 7:")
print(routing.bestpath(g,0,7))

