"""
a_star_shortest_path.py


"""
import heapq
from collections import defaultdict
from math import sqrt
from graph_data import *


# ----------------------------------------------------------------------
# Kind of follows the pseudocode described here:
#    https://en.wikipedia.org/wiki/A*_search_algorithm
# ----------------------------------------------------------------------
def shortest_path(mapx, start, goal):
    print("shortest path called")
    # set of already discovered nodes
    #openSet = PriorityQueue()
    #openSet.put(start, 0) # start at the beginning!
    openSet = set()
    openSet.add(start)

    # for node n, came_from[n] is node immediately preceding it on the
    # cheapest path from start to n currently known
    #came_from = []
    came_from = defaultdict()

    closed_set = set()

    # node n, act_cost[n] is the cost of the cheapest path from start to
    # n that is currently known or distance between start to current.
    act_cost = defaultdict()
    act_cost[start] = 0 # math.inf # default value of infinity

    # for node n, total cost of the node, tot_cost[n] := act_cost[n] + h(n)
    tot_cost = defaultdict()
    tot_cost[start] = (act_cost[start] +
    calc_distance(mapx.intersections[start], mapx.intersections[goal]))

    current = start

    while len(openSet) > 0: # not openSet.empty(): # if not empty
        print("<<<<< TESTING >>>>>")
        print("openSet:", openSet)
        print("came_from:", came_from)
        print("act_cost:", act_cost)
        print("tot_cost:", tot_cost)

        # --- test block ---
        if current in openSet:
            openSet.remove(current)

        closed_set.add(current)

        if current == goal:
            best_path = []
            # this is a kludge to get the best path in proper order
            for x in closed_set:
                best_path.append(x)
            kludge = [best_path[0]]
            kludge += best_path[:0:-1]
            print("best_path", kludge)
            return kludge

        # keep searching in connected edges/roads
        for road in mapx.roads[current]:
            print("  => current, road", current, road)

            if road in closed_set:
                continue    # already used, keep moving

            # cost from current to neighbor
            neighbor_cost = calc_distance(mapx.intersections[current], mapx.intersections[road])

            # distance/cost from start to the neighbor through current
            gScore_possible = act_cost[current] + neighbor_cost

            act_cost[road] = neighbor_cost
            print("     **********")
            print("     neighbor_cost", neighbor_cost)
            print("     gScore_possible", gScore_possible)
            print("     act_cost[road]", act_cost[road])

            if road not in openSet or gScore_possible < act_cost[road]:
                # this is better than previous path, record it
                gScore_possible = act_cost[current] + neighbor_cost
                came_from[road] = act_cost[current]
                act_cost[road] = gScore_possible
                tot_cost[road] = act_cost[current] + calc_distance(mapx.intersections[road], mapx.intersections[goal])

                openSet.add(road)
                current = road
    # open set is empty but goal was not found
    return None


# ----------------------------------------------------------------------
def calc_distance(point_xy1, point_xy2):
    # broken out for clarity
    x1 = point_xy1[0]
    y1 = point_xy1[1]
    x2 = point_xy2[0]
    y2 = point_xy2[1]
    # print("x2={} x1={} y2={} y1={}".format(x2, x1, y2, y1))
    return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
# ----------------------------------------------------------------------


if __name__ == "__main__":
    m40 = Map40()

    #print(shortest_path(m40, 5, 34) == [5, 16, 37, 12, 34])
    #print(shortest_path(m40, 8, 24) == [8, 14, 16, 37, 12, 17, 10, 24])
    #print(shortest_path(m40, 5, 5) == [5])

    m10 = Map10()

    """
    print(shortest_path(m10, 0, 2) == [5, 3, 2])
    print("-"*105)
    for i in range(len(m10.roads)):
        print("m10: intersection {}: {} connected to {} road(s)".format(i, m10.intersections[i], m10.roads[i]))

    print("-"*105)
    dist = calc_distance(m10.intersections[0], m10.intersections[5])
    tot_dist = dist
    print("distance between node 0 and 5 is", dist)

    dist = calc_distance(m10.intersections[5], m10.intersections[3])
    tot_dist += dist
    print("distance between node 5 and 3 is", dist)

    dist = calc_distance(m10.intersections[3], m10.intersections[2])
    tot_dist += dist
    print("distance between node 3 and 2 is", dist)

    print("total distance from node 0 to 2 is", tot_dist)
    """

    print("-"*105)
    #print("shortest_path(m10, 0, 2) is [0, 5, 3, 2]:", shortest_path(m10, 0, 2) == [0, 5, 3, 2])
    print("shortest_path(m10, 0, 2) is [0, 5, 3, 2]:", shortest_path(m10, 0, 2))
    print("-"*105)
    #print("shortest_path(m10, 6, 8) is None:", shortest_path(m10, 6, 8) == None)

