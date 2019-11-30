"""
ax_star_shortest_path.py

LOOK AT:
http://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/
https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb

!!!
examine cost
https://rosettacode.org/wiki/A*_search_algorithm#Python
http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/

*********************************************************************
change the damn names to match so it's easier to compare
https://www.redblobgames.com/pathfinding/a-star/introduction.html

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break

   for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current

"""
import heapq
from collections import defaultdict
from math import sqrt
from graph_data import *


"""
----------------------------------------------------------------------
Kind of follows the pseudocode described here:
  https://en.wikipedia.org/wiki/A*_search_algorithm

But also like this:
  http://csis.pace.edu/~benjamin/teaching/cs627/webfiles/Astar.pdf

Which has a similar implementation in Python here:
  https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
----------------------------------------------------------------------
"""
def shortest_path(mapx, start, goal):
    # set of already discovered nodes
    open_set = set()
    open_set.add(start) # start at the beginning!

    # for node n, came_from[n] is node immediately preceding it on the
    # cheapest path from start to n currently known
    came_from = defaultdict()

    closed_set = set()

    # node n, act_cost[n] is the cost of the cheapest path from start to
    # n that is currently known or distance between start to current.
    act_cost = 0
    est_cost = calc_distance(mapx.intersections[start], mapx.intersections[goal]) # 0

    # this def needs a better name, but it came by FUBAR due to the
    # fact that this was the state of this code until I added it
    # and pushed the items onto the heap
    fubar = []
    heapq.heappush(fubar, (est_cost, start, act_cost))

    # for node n, total cost of the node, tot_cost[n] := act_cost[n] + h(n)
    tot_cost = defaultdict()
    tot_cost[start] = calc_distance(mapx.intersections[start], mapx.intersections[goal])

    while len(open_set) > 0:
        est_cost, current, act_cost = heapq.heappop(fubar)
        """
        print("<<<<< TESTING >>>>>")
        print("open_set:", open_set)
        print("closed_set:", closed_set)
        print("came_from:", came_from)
        print("act_cost:", act_cost)
        print("est_cost:", est_cost)
        print("tot_cost:", tot_cost)
        print("fubar:", fubar)
        """

        if current in open_set:
            open_set.remove(current)

        if current == goal:
            #return a_star_search_path(came_from, current)
            """
            best_path = []
            for current in came_from.keys():
                current = came_from[current]
                if current not in best_path:
                    best_path.append(current)
            best_path.append(goal)
            return best_path
            """
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            #path.reverse() # optional
            return path[::-1]

        closed_set.add(current)

        # keep searching in connected edges/roads
        for road in mapx.roads[current]:
            if road not in closed_set:
                #print("  => current, road", current, road)

                # cost from current to neighbor
                #new_cost = act_cost + calc_distance(mapx.intersections[current], mapx.intersections[road])
                new_cost = act_cost + calc_distance(mapx.intersections[current], mapx.intersections[road])

                # distance/cost from start to the neighbor through current
                #cost_from_neighbor = act_cost + calc_distance(mapx.intersections[road], mapx.intersections[goal])
                #cost_from_neighbor = new_cost + calc_distance(mapx.intersections[road], mapx.intersections[goal])
                #cost_from_neighbor = calc_distance(mapx.intersections[road], mapx.intersections[goal])
                #cost_from_neighbor = get_neighbor_cost(fubar, road)
                cost_from_neighbor = act_cost + calc_distance(mapx.intersections[current], mapx.intersections[road])

                #act_cost = new_cost
                """
                print("     **********")
                print("     new_cost", new_cost)
                print("     cost_from_neighbor", cost_from_neighbor)
                print("     act_cost[road]", act_cost[road])
                """
                if road not in open_set or new_cost < cost_from_neighbor: #act_cost[road]:
                    # record it
                    cost_from_neighbor = new_cost # is this necessary?
                    came_from[road] = current
                    #tot_cost[road] = new_cost + calc_distance(mapx.intersections[road], mapx.intersections[goal])
                    tot_cost[road] = new_cost + calc_distance(mapx.intersections[road], mapx.intersections[goal])

                    heapq.heappush(fubar, (tot_cost[road], road, cost_from_neighbor))
                    open_set.add(road)

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


def get_neighbor_cost(priority_queue, neighbor):
    for i in priority_queue:
        #print("get_neighbor_cost:priority_queue", priority_queue)
        if i[1] == neighbor:
            item = priority_queue[0][2]
            #print("*"*25)
            #print("get_neighbor_cost: i={} neighbor={}".format(i, neighbor))
            #print("get_neighbor_cost: item={}".format(item))
            #print("*"*25)
            return item


def a_star_search_path(came_from, current):
    path = [current]
    #print("current:", current)
    while current in came_from.keys():
        current = came_from[current]
        #print("current:", current, came_from)
        path.append(current)
    #print("path:", path)
    return path[::-1]

# ----------------------------------------------------------------------


def main():
    m40 = Map40()

    print(shortest_path(m40, 5, 34) == [5, 16, 37, 12, 34])
    print("shortest_path(m40, 5, 34) = [5, 16, 37, 12, 34]:", shortest_path(m40, 5, 34))
    print("shortest_path(m40, 8, 24) == [8, 14, 16, 37, 12, 17, 10, 24]", shortest_path(m40, 8, 24))
    print(shortest_path(m40, 5, 5) == [5])

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
    print("shortest_path(m40, 5, 34) == [5, 16, 37, 12, 34]:", shortest_path(m40, 5, 34))
    print("shortest_path(m40, 5, 5) = [5]:", shortest_path(m40, 5, 5))
    print("shortest_path(m10, 6, 8) is None:", shortest_path(m10, 6, 8) == None)
    print("-"*105)

if __name__ == "__main__":
    main()
