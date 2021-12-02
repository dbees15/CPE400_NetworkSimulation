import networkx
import routing
import random


#==========Script Body==========

sim_num = 5000    #number of times to run simulaiton
max_power = 3000    #maximum power possible for a node. must be factor of 100
graph_generator = routing.generate_graph_6  #generator for graph

#==========Simulation for 6 node graph==========
print("===Tests for 6 node graph===")

#run sim with reroute=True
resultlist = [] #list of packets sent for each sim
rl = []
for i in range(0,sim_num):  #run simulation sim_num number of times
    result,reroute_num = routing.simulate(graph_generator,max_power,True,0,5,100)
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
    result,reroute_num = routing.simulate(graph_generator,max_power,False,0,5,100)
    resultlist.append(result)
    rl.append(reroute_num)

average = sum(resultlist) / len(resultlist) #take averages of results
r_average = sum(rl) / len(rl)

print(f"\nSimulation results with reroute disabled")
print(f"Average: {average}")
print(f"Average Reroutes: {r_average}")

resultlist.clear()  #clean up
rl.clear()



#==========Simulation for 8 node graph==========
print("\n===Tests for 8 node graph===")

graph_generator = routing.generate_graph_8

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

print(f"\nSimulation results with reroute disabled")
print(f"Average: {average}")
print(f"Average Reroutes: {r_average}")

resultlist.clear()  #clean up
rl.clear()




#==========Simulation for 10 node graph==========
print("\n===Tests for 10 node graph===")

graph_generator = routing.generate_graph_10

#run sim with reroute=True
resultlist = [] #list of packets sent for each sim
rl = []
for i in range(0,sim_num):  #run simulation sim_num number of times
    result,reroute_num = routing.simulate(graph_generator,max_power,True,0,9,100)
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
    result,reroute_num = routing.simulate(graph_generator,max_power,False,0,9,100)
    resultlist.append(result)
    rl.append(reroute_num)

average = sum(resultlist) / len(resultlist) #take averages of results
r_average = sum(rl) / len(rl)

print(f"\nSimulation results with reroute disabled")
print(f"Average: {average}")
print(f"Average Reroutes: {r_average}")

resultlist.clear()  #clean up
rl.clear()
