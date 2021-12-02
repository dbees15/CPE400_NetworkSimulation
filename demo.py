import networkx
import routing
import random


def tests(graph_generator,targetnode,nodenum,max_power,sim_num):
    print(f"\n===Tests for {nodenum} node graph===")

    #run sim with reroute=True
    resultlist = [] #list of packets sent for each sim
    rl = []
    for i in range(0,sim_num):  #run simulation sim_num number of times
        result,reroute_num = routing.simulate(graph_generator,max_power,True,0,targetnode,100)
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
        result,reroute_num = routing.simulate(graph_generator,max_power,False,0,targetnode,100)
        resultlist.append(result)
        rl.append(reroute_num)

    average = sum(resultlist) / len(resultlist) #take averages of results
    r_average = sum(rl) / len(rl)

    print(f"\nSimulation results with reroute disabled")
    print(f"Average: {average}")
    print(f"Average Reroutes: {r_average}")

    resultlist.clear()  #clean up
    rl.clear()



#==========Script Body==========

sim_num = 6000    #number of times to run simulaiton
max_power = 3000    #maximum power possible for a node. must be factor of 100
graph_generator = routing.generate_graph_6  #generator for graph

#==========Simulation for 6 node graph==========
tests(routing.generate_graph_6,5,6,max_power,sim_num)

#==========Simulation for 8 node graph==========
tests(routing.generate_graph_8,7,8,max_power,sim_num)

#==========Simulation for 10 node graph==========
tests(routing.generate_graph_10,9,10,max_power,sim_num)

#==========Simulation for 12 node graph==========
tests(routing.generate_graph_12,11,12,max_power,sim_num)
