"""
Stack class has the following behaviors:

    push - adds an item to the top of the stack
    pop - removes an item from the top of the stack (and returns the value of that item)
    size - returns the size of the stack
    top - returns the value of the item at the top of stack (without removing that item)
    is_empty - returns True if the stack is empty and False otherwise

"""

class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        """
        The method will need to have a parameter for the value that you want to push
        Remember that next_index will have the index for where the value should be added
        Once you've added the value, you'll want to increment both next_index and num_elements

        Provide a conditional check to see if array is full and increase it's size
        """
        if self.next_index == len(self.arr):
            print("Yikes, out os stack space! Increasing capacity...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        """
        copy contents of stack array to temp array
        double the size of stack array
        copy contents back into stack array
        *** not efficient (time complexity) ***
        """
        old_arr = self.arr
        self.arr = [0 for _ in range( 2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        # [on_true] if [expression] else [on_false]
        return (True if self.num_elements == 0 else False)

    def pop(self):
        """
        Check if the stack is empty and, if it is, return None
        Decrement next_index and num_elements
        Return the item that is being "popped"
        *** note the item is replaced with a 0 in this case ***
        """
        if self.is_empty():
            self.next_index = 0
            return None
        self.num_elements -= 1
        self.next_index -= 1
        popped = self.arr[self.next_index]
        self.arr[self.next_index] = 0
        return popped

foo = Stack()
print(foo.arr)
foo.push("test")
foo.push(101)
foo.push("fuken-a")
foo.push("text")
foo.push(99)
foo.push("fuken-puken")
foo.push("temp")
foo.push(42)
foo.push("fuken-gruven")
foo.push("trax")
foo.push(9)
foo.push("fuken-postal")
print(foo.arr)
print(foo.num_elements)
print("~"*25)
print(foo.pop())
print(foo.arr)
print(foo.num_elements)
