"""
graph_bfs_iteration.py

"""

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self,new_node):
        self.children.append(new_node)

    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list

    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


def bfs_search(root_node, search_value):
    visited = []
    queue = [root_node]

    while len(queue) > 0:
        current_node = queue.pop(0)
        queue.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)


print( bfs_search(nodeS, 'A') )
print( bfs_search(nodeP, 'S') )
print( bfs_search(nodeH, 'R') )


# iterate through the GraphNode children
graph_node = bfs_search(nodeH, 'R')
print("\nGraph Node Parent Value =", graph_node.value)
print("Children (connections):")
for child in graph_node.children:
    print(child.value, end=' ')
print(" ")


# this hangs up if passed a search value that doesn't exist in graph
#print( bfs_search(nodeH, 'I') )

def bfs(graph, initial):
    # works for dictionary
    visited = []
    queue = [initial]

    while queue:
        node = queue.pop(0)
        if node not in visited:

            visited.append(node)

            if node not in graph:
                print("Sorry, '{}' is not in graph".format(node))
                return None

            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

print("\nGraph built with a dictionary:")
print("= - = "*15)
print( bfs(graph, 'G') )

























