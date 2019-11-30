"""
student_code.py

References:
  https://www.redblobgames.com/pathfinding/a-star/implementation.html

"""

import heapq
from collections import defaultdict
from math import sqrt
from graph_data import *

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# ----------------------------------------------------------------------
def calc_distance(point_xy1, point_xy2):
    # broken out for clarity
    x1 = point_xy1[0]
    y1 = point_xy1[1]
    x2 = point_xy2[0]
    y2 = point_xy2[1]
    # print("x2={} x1={} y2={} y1={}".format(x2, x1, y2, y1))
    return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )


def shortest_path(mapx, start, goal):
    # farthest points or paths already explored
    frontier = PriorityQueue()
    frontier.put(start, 0)

    # points or paths prior to paths in the frontier
    explored = {}
    explored[start] = None

    # unexplored - points/paths after the frontier
    # not needed, just here for documentation/understanding the algorithm
    unexplored = None

    """
    G: cost so far = distance between the start node and current node
    H: estimated cost = estimated distance from current node to the end node
    F: total cost = G + H
    """
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            best_path = []
            # backtrack through the explored points
            while current != start:
                best_path.append(current)
                current = explored[current]
            best_path.append(start)
            # reverse it -> start to goal
            return best_path[::-1]

        for next_road in mapx.roads[current]:
            # g_score_possible = total cost through the current point/road to the next point/road
            g_score_possible = cost_so_far[current] + calc_distance(mapx.intersections[current], mapx.intersections[next_road])
            if next_road not in cost_so_far or g_score_possible < cost_so_far[next_road]:
                # best path so far so record it
                cost_so_far[next_road] = g_score_possible
                # cost value used as minimum priority for the heapq (min heap)
                cost_value = g_score_possible + calc_distance(mapx.intersections[next_road], mapx.intersections[goal])
                frontier.put(next_road, cost_value)
                explored[next_road] = current
    # uh oh, frontier is empty but goal was not found
    return None

def main():
    m40 = Map40()
    m10 = Map10()
    print("shortest_path(m10, 0, 2) = [0, 5, 3, 2]:", shortest_path(m10, 0, 2))
    print("shortest_path(m40, 5, 34) = [5, 16, 37, 12, 34]:", shortest_path(m40, 5, 34))
    print("shortest_path(m40, 8, 24) = [8, 14, 16, 37, 12, 17, 10, 24]", shortest_path(m40, 8, 24))
    print("shortest_path(m40, 5, 5) = [5]:", shortest_path(m40, 5, 5))
    print("shortest_path(m10, 6, 8) = None:", shortest_path(m10, 6, 8))

if __name__ == "__main__":
    main()
