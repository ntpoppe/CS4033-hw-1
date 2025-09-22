import math
from collections import deque
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
def heuristic2(goal, romania_adj_list):
    cities_list = romania_adj_list.keys()
    h = {}

    for city in cities_list:
        if city == goal:
            h[city] = 0 #the heuristic for the goal is always 0
        else:
            neighbors = romania_adj_list[city]
            estimates = []
            for neighbor, dist in neighbors.items(): 
                neighbor_est = 0 if neighbor == goal else hSLD_bucharest.get(neighbor, 999) #if neighbor is the goal use edge distanc, else use SLD
                estimates.append(dist + neighbor_est)
                #choose the smallest estimate
            h[city] = min(estimates) if estimates else 9999 #if there are no neighbors use fallback num
    return h

def heuristic2(goal, romania_adj_list):
    # find the smallest edge in the graph
    min_edge = min(distance for city in romania_adj_list for distance in romania_adj_list[city].values())
    
    # compute min numner of hops from every city to the goal
    hop_distance = {city: float("inf") for city in romania_adj_list}
    hop_distance[goal] = 0
    queue = deque([goal])
    #using BFS to compute
    while queue:
        city = queue.popleft()
        for neighbor in romania_adj_list[city]:
            if hop_distance[neighbor] == float("inf"):#if city hasn't been visited yet set the hop distance to current city+1
                hop_distance[neighbor] = hop_distance[city] + 1
                queue.append(neighbor)
    
    #hops to goal* min edge cost
    h = {city: hop_distance[city] * min_edge for city in romania_adj_list}
    return h




