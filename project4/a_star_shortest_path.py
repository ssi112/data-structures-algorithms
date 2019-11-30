"""
a_star_shortest_path.py


"""
import heapq
from collections import defaultdict
from math import sqrt
from graph_data import *


"""
min priority queue - lower priority elements are added to the front
    of the queue (smaller numbers have higher priority)

elements are added or removed based on priority

priority is set and elements are added at the proper position

when dequeued, the item with highest priority is removed first

the queue will remain sorted by priority
"""


class QueueElement(object):
    element = ""
    priority = 0.0

    def __init__(self, element = None, priority = None):
        self.element = element
        self.priority = priority


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, element, priority):
        queueElement = QueueElement(element, priority)
        if self.isEmpty():
            # push the first item onto the queue
            self.queue.append(queueElement)
        else:
            added = False
            for inx, queueItem in enumerate(self.queue):
                if queueElement.priority < queueItem.priority:
                    # insert the new element one position before
                    # respects other elements with same priority
                    # but were added first
                    # inx = index and where to insert new element
                    self.queue.insert(inx, queueElement)
                    added = True
                    # stop searching
                    break
            if added == False:
                # if no other elements are greater than this element's
                # priority then add it to the end of the queue
                self.queue.append(queueElement)

    def dequeue(self):
        # remove & return highest priority item
        return self.queue.pop(0)

    def removeLowestPriorityItem(self):
        # this will remove and return lowest priority item
        # used if size is fixed and space is needed
        lastItem = self.queue[-1]
        del self.queue[-1]
        return lastItem

    def front(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def clearQueue(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return ''.join([str(inx) + '-' + str(queueItem.priority) + '-' +
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


# ----------------------------------------------------------------------
def shortest_path(mapx, start, goal):
    # set of already discovered nodes
    #open_set = PriorityQueue()
    #open_set.put(start, 0) # start at the beginning!
    open_set = []
    open_set_pq = PriorityQueue()


    # for node n, came_from[n] is node immediately preceding it on the
    # cheapest path from start to n currently known
    came_from = defaultdict()
    came_from[start] = None

    # node n, act_cost[n] is the cost of the cheapest path from start to
    # n that is currently known or distance between start to current.

    # for node n, total cost of the node, tot_cost[n] := act_cost[n] + h(n)
    act_cost = defaultdict()
    act_cost[start] = 0 # math.inf # default value of infinity
    tot_cost = {}

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    heapq.heappush(open_set, (act_cost, start))

    open_set_pq.enqueue(start, act_cost)

    while open_set_pq.size() > 0: # len(open_set) > 0:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        act_cost, current = heapq.heappop(open_set)
        lowestRemoved = open_set_pq.removeLowestPriorityItem()
        current, act_cost[current] = lowestRemoved.element, lowestRemoved.priority
        print("lowestRemoved", lowestRemoved.element, lowestRemoved.priority)
        print("current, act_cost[current]", current, act_cost[current])

        print("_"*55)
        print("current, act_cost[current]", current, act_cost[current])
        print("_"*55)
        #break

        #print("act_cost={}  [---]  current={}".format(act_cost, current))

        if current == goal:
            best_path = []
            while current != start:
                best_path.append(current)
                current = came_from[current]
            best_path.append(start)
            #print("open_set", open_set)
            return best_path[::-1]

        # keep searching in connected edges/roads
        for road in mapx.roads[current]:
            #print("  => current, road", current, road)

            # cost through current to neighbor
            g_score_possible = act_cost[current] + calc_distance(mapx.intersections[current], mapx.intersections[road])

            if road not in act_cost or g_score_possible < act_cost[road]:
                # this is better than previous path, record it
                act_cost[road] =  g_score_possible
                cost_val = g_score_possible + calc_distance(mapx.intersections[road], mapx.intersections[goal])
                tot_cost[road] = cost_val
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #print("act_cost={}  [---]  cost_val={}".format(act_cost, cost_val))
                #heapq.heappush(open_set, (tot_cost, road))
                open_set_pq.enqueue(road, cost_val)
                came_from[road] = current
    # open set is empty but goal was not found
    return None


def main():
    m40 = Map40()
    m10 = Map10()
    print("shortest_path(m10, 0, 2) = [0, 5, 3, 2]:", shortest_path(m10, 0, 2))
    #print("shortest_path(m40, 5, 34) = [5, 16, 37, 12, 34]:", shortest_path(m40, 5, 34))
    #print("shortest_path(m40, 8, 24) = [8, 14, 16, 37, 12, 17, 10, 24]", shortest_path(m40, 8, 24))
    #print("shortest_path(m40, 5, 5) = [5]:", shortest_path(m40, 5, 5))
    #print("shortest_path(m10, 6, 8) = None:", shortest_path(m10, 6, 8))

if __name__ == "__main__":
    main()


