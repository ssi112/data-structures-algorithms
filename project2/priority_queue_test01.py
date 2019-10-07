"""
priority_queue_test01.py

some tests for priority_queue.py

TESTING 1, 2, 3
see https://repl.it/@ssi112/PriorityQueue for similar testing

"""
import sys
from priority_queue import *

# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

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

