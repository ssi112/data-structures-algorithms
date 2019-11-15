"""
connecting_islands.py

In an ocean, there are n islands some of which are connected via bridges.
Travelling over a bridge has some cost attached with it. Find bridges in
such a way that all islands are connected with minimum cost of travelling.

You can assume that there is at least one possible way in which all
islands are connected with each other.

You will be provided with two input parameters:

    num_islands = number of islands

    bridge_config = list of lists. Each inner list will have 3 elements:

     a. island A
     b. island B
     c. cost of bridge connecting both islands

    Each island is represented using a number

Example:

    num_islands = 4
    bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

Input parameters explanation:

1. Number of islands = 4
2. Island 1 and 2 are connected via a bridge with cost = 1
   Island 2 and 3 are connected via a bridge with cost = 4
   Island 1 and 4 are connected via a bridge with cost = 3
   Island 4 and 3 are connected via a bridge with cost = 2
   Island 1 and 3 are connected via a bridge with cost = 10

In this example if we are connecting bridges like this...

    between 1 and 2 with cost = 1
    between 1 and 4 with cost = 3
    between 4 and 3 with cost = 2

...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.
"""

import heapq

heap = []

print("the heap! {}".format(heap))

bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
print("\nbridge_config (before)", bridge_config)

# sort in place on index 0 of each list
bridge_config.sort(key=lambda x: x[0])
print("bridge_config (after)", bridge_config)

for bridges in bridge_config:
    heapq.heappush(heap, bridges)

print("\nthe new and improved heap! {}".format(heap))


# ------------------------------------------------------------------------
# Makes use of one of Python's PriorityQueue implementation (heapq)
# For more details -
#   https://thomas-cokelaer.info/tutorials/python/module_heapq.html
# ------------------------------------------------------------------------

def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    adjacency_list = [list() for _ in range(num_islands + 1)]

    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    #print("adjacency_list",adjacency_list)
    return adjacency_list



def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True
    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the
            problem statement
    return: cost (int) minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


# >>>>> TEST IT <<<<<
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

result = get_minimum_cost_of_connecting(num_islands, bridge_config)
print("\nNumber of islands =", num_islands)
print("Bridge configuration:", bridge_config)
print("Solution should = {} Result = {}".format(solution, result))

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

result = get_minimum_cost_of_connecting(num_islands, bridge_config)
print("\nNumber of islands =", num_islands)
print("Bridge configuration:", bridge_config)
print("Solution should = {} Result = {}".format(solution, result))

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

result = get_minimum_cost_of_connecting(num_islands, bridge_config)
print("\nNumber of islands =", num_islands)
print("Bridge configuration:", bridge_config)
print("Solution should = {} Result = {}".format(solution, result))
