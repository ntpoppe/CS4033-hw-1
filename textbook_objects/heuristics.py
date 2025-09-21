import math
# heuristic from textbook: straight line distances to Bucharest
hSLD_bucharest = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80,
    "Vaslui": 199, "Zerind": 374
}

# this heuristic is created by finding the shortest distance path each city in the adjacency list to the goal city.
# It will calculate the shortest path backward from the source so the goal distance is zero initially.
# what it does is it will loop through each neighboring city of the current city in the list and check the distance to the neighbor,
# if it finds a short path, it will change the distance intil the shotrest path is found.
def heuristic1(goal, romania_adj_list):
    # this will give us a list of the cities in the adjaceny list of Romania
    cities_list = romania_adj_list.keys()
    h ={}
    # all the distances will be set to infinity initially because according to the lab document, 
    # we use infinity to represent a very lage value when we don't know the exact distance
    for city in cities_list:
        h[city] = math.inf
    h[goal] = 0

    # we are checking if the distance has changed (if a shorter path has been formed)
    distance_changed = True
    while distance_changed == True:
        distance_changed = False

        # for each city in the list
        for city in cities_list:
            # get all of the neighboring cities of that cities
            neighbors = romania_adj_list[city]
            for neighbor in neighbors:
                distance = neighbors[neighbor]
            
            # if you find a shorter path the shortest distance is changed to that path length
            if h[city] > h[neighbor] + distance:
                h[city] = h[neighbor] + distance
                distance_changed = True
    return h



