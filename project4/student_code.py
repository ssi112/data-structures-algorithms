"""
student_code.py

Explanation & pseudocode
  https://en.wikipedia.org/wiki/A*_search_algorithm

Uses a min priority queue to keep track of the least
cost/distance values of the paths to each point.
"""

from math import sqrt
# below used to run from python command line
from graph_data import *

# ----------------------------------------------------------------------
class Queue_Element(object):
    element = ""
    priority = 0.0

    def __init__(self, element = None, priority = None):
        self.element = element
        self.priority = priority


class Min_Priority_Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, element, priority):
        queue_element = Queue_Element(element, priority)
        if self.is_empty():
            # push the first item onto the queue
            self.queue.append(queue_element)
        else:
            added = False
            for inx, queueItem in enumerate(self.queue):
                if queue_element.priority < queueItem.priority:
                    # insert the new element one position before
                    # respects other elements with same priority
                    # but were added first
                    # inx = index and where to insert new element
                    self.queue.insert(inx, queue_element)
                    added = True # stop searching
                    break
            if added == False:
                # if no other elements are greater than this element's
                # priority then add it to the end of the queue
                self.queue.append(queue_element)

    def dequeue(self):
        # this will remove and return the first/lowest priority item
        return self.queue.pop(0)

    def __repr__(self):
        return ''.join([str(inx) + ' - ' + str(queueItem.priority) + ' - ' +
            str(queueItem.element) + '\n' for inx, queueItem in enumerate(self.queue)])


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
    # farthest points or paths already explored a.k.a the frontier
    open_set_pq = Min_Priority_Queue()
    open_set_pq.enqueue(start, 0)

    # points or paths prior to the paths in the frontier (open set)
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

    while not open_set_pq.is_empty():
        lowestRemoved = open_set_pq.dequeue()
        current, l_priority = lowestRemoved.element, lowestRemoved.priority
        #print("*"*75)
        #print("current={} || l_priority={}".format(current, l_priority))

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
                # cost value used as minimum priority for the priority queue
                cost_value = g_score_possible + calc_distance(mapx.intersections[next_road], mapx.intersections[goal])
                # push this one onto the queue
                open_set_pq.enqueue(next_road, cost_value)
                #print("next_road={} | cost_value={}".format(next_road, cost_value))
                explored[next_road] = current
    # uh oh, open_set_pq is empty but goal was not found
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
