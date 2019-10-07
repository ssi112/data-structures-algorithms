"""
priority_queue.py

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
        return ''.join([str(inx) + '-' + str(queueItem.priority) + '-' + str(queueItem.element) + '\n' for inx, queueItem in enumerate(self.queue)])

#
# TESTING 1, 2, 3
# see https://repl.it/@ssi112/PriorityQueue for other testing
#
pq = PriorityQueue()

pq.enqueue("John", 2);
pq.enqueue("Jack", 1);
pq.enqueue("Camila", 1);
pq.enqueue("Esteban", 3)

print()
print("Is queue empty?", pq.isEmpty())
print("What is the size of queue?", pq.size())
hpi = pq.front()
print("Highest priority item is {} at priority {}".format( hpi.element, hpi.priority) )

print("adding Esperanaza 4...")
pq.enqueue("Esperanaza", 4)
print("\n.....current priority queue.....")
print(pq)

print()
print("adding Hayleigh 0.05...")
pq.enqueue("Hayleigh", 0.05)

print()
print("\n.....current priority queue.....")
print(pq)

print()
print("adding Rachele 9...")
pq.enqueue("Rachele", 9)
print("What is the size of queue?", pq.size())
print("\n.....current priority queue.....")
print(pq)

print()
print("adding Robin 7...")
pq.enqueue("Robin", 7)
print("\n.....current priority queue.....")
print(pq)

print()
print("Removing lowest priority item...")
lowestRemoved = pq.removeLowestPriorityItem()
print(lowestRemoved.element, lowestRemoved.priority)
print("\n.....current priority queue.....")
print(pq)


