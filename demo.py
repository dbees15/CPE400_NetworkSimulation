import networkx
import routing
import random


#==========Script Body==========

sim_num = 2000    #number of times to run simulaiton
max_power = 3000    #maximum power possible for a node. must be factor of 100
graph_generator = routing.generate_graph_8  #generator for graph

#run sim with reroute=True
resultlist = [] #list of packets sent for each sim
rl = []
for i in range(0,sim_num):  #run simulation sim_num number of times
    result,reroute_num = routing.simulate(graph_generator,max_power,True,0,7,100)
    resultlist.append(result)
    rl.append(reroute_num)

average = sum(resultlist) / len(resultlist) #take averages of results
r_average = sum(rl) / len(rl)

print(f"Simulation results with reroute enabled")
print(f"Average: {average}")
print(f"Average Reroutes: {r_average}")

resultlist.clear()  #clean up
rl.clear()



#run sim with reroute=False
resultlist = [] #list of packets sent for each sim
rl = []
for i in range(0,sim_num):  #run simulation sim_num number of times
    result,reroute_num = routing.simulate(graph_generator,max_power,False,0,7,100)
    resultlist.append(result)
    rl.append(reroute_num)

average = sum(resultlist) / len(resultlist) #take averages of results
r_average = sum(rl) / len(rl)

print(f"Simulation results with reroute disabled")
print(f"Average: {average}")
print(f"Average Reroutes: {r_average}")

resultlist.clear()  #clean up
rl.clear()
