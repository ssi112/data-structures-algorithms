#1 LRU Cache
Uses Pythons's OrderedDict as cache, which keeps track of the order that
entries are inserted. Deleting an entry and reinserting it will move it to the end.
If the value of a key is changed, the key position does not change. Ordered Dictionaries are implement as hash tables. Reference https://mail.python.org/pipermail/python-dev/2017-December/151283.html. Hash tables should provide average O(1) for search, insertion and deletion. If m is the size of the data stored in the cache then each set operation will cause it to grow by m up to the maximum size of the cache capacity: O(m*m), n being the cache capacity.


#2 File Recursion
Uses a list containing the paths as the problem called for it. Lists work well for this problem as they provide quick access and ease of iteration to display output and also to build the list. Appending to a list is O(1) while extending a list is O(k) - 'k' in this case should be the number of elements.

Recursion was used, again as the problem called for it, however recursion does use additional overhead as it requires additional stack space for the functions arguments, rewinding the stack, passing control back to where the function was called, etc. Also, requires some additional time to complete these steps. This particular problem does not have a deep directory structure. The memory or space used is based on the number of recursive calls, which determines the number of stack frames times the space required for each stack frame. That would be O(n*m) if n is the number of calls and m being the space required for each frame.


#3 Huffman Encoding
I used a tree. Why? Because the problem stated, "Build the Huffman Tree". So the tree holds the letters and counts. Trees typically have O(log(n)) time for accessing, insertion and deletion on average. worst case is O(n) - n being the number of nodes in the tree.

There are other structues in here as well: a dictionary to keep track of the letters and counts - O(1) average, O(n) worst case as when the dict is iterated over to create a list of tuples.

There is also a priority queue: O(n) worst case for access and searching, O(1) inserting. A priority queue works well for this problem because it keeps track of the minimum value. Items with highest priority are dequeued before those with lower priorities. Items with same priority are served according to their order in the queue. This takes care of some of the work managing the nodes of the tree.

During encoding each iteration of a tree node adds one element to the dictionary so it grows by number (n) of items being encoded plus the size of the encoding string which is related to the depth or number of levels (d) in the tree: O(n+d). Decoding requires rebuilding the output string to the same size (n) as the original data provided: O(n).


#4 Active Directory
Decided to use a set for groups and users as they have a bit less overhead than lists and are faster. Though, because the small size for testing purposes the actual time difference was so minor not to be noticed. They also don't allow for duplicates, which seems like something needed if storing actual user IDs. Function is_user_in_group(): searching through set using x in s, which this does, averages O(1) while worst case is O(n). At least in this example we are not concerned about the order the entries are stored in and a set accommodates that well. If the initial group being searched contains a sub-group then a recursive call is made to search that group for the user. There are some basic operations within the function: setting a flag, checking if the user is in the group (O(1) search time) and determining whether the object is a Group before making the recursive call, so only if needed is a recursive call made.

Most of the time is spent in the is_user_in_group() function; time complexity discussed above. The only additional overhead of memory added to execute this function is a single boolean flag to indicate whether the user exists in the group or any sub-groups: O(1).


#5 Blockchain
The problem calls for a linked list. Hmm, I'm noticing a pattern here. This is a singly linked list that maintains a tail pointer. New blocks are appended and the tail always points to the most recently added block. There is a previous pointer within the blocks  themselves so traversal backwards through the block chain is possible. Insertions have average and worst case Big O(1) while searching requires O(n). If there are n items in the list (blockchain) and each item takes up m amount of memory the space complexity would be O(n*m). As a side note the data stored is simply a random integer.

#6 Union & Intersection
Here again the problem calls for using linked lists to mimic the actions of a set's methods for union and intersection. Insertions and deletions (deletes not done in this example) have average and worst case Big O(1). A method of finding whether a value is in the list is implemented (in_list) and this can require O(n) in order to find an item as it may have to search the entire list/chain.

To implement the union and intersect method requires multiple searches. For instance, the union goes through each list element by element O(n) and searches for it in the union list to avoid duplicates. The union list search, worst case, O(n) so worst case for both union and intersection could be O(n^2). The intersect goes through one list element by element, O(n) and searches for it in the second list and also in the intersect list before it adds it - worst case O(n^2) for each search. The space complexity for both could conceivably require adding all elements from the lists to either the union or intersection, worst case O(n^2).



