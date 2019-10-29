# Project #3

## <span style="text-decoration: underline">Requirements</span>

### Data Structure Questions

For this project, you will answer the seven questions laid out in the next sections. The questions cover a variety of topics related to the basic algorithms you've learned in this course. You will write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices.


---

**Python Big O Reference Information:**

 - [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
 - [All You Need to Know About Big O Notation](https://skerritt.blog/big-o/)
 - [Big O Notation & Algorithm Analysis](https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/)

---

## Problem #1: Finding the Square Root of an Integer

### Design
The sqrt() functions uses the [Babylonian method](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
) as described in the Wikipedia article. This performed slightly better then a binary method for large numbers. There was tweaking done in both methods, however, if the binary method was not tweaked to begin at the mid-point it performed significantly worse on larger numbers. I believe it performs better then binary due to converging on the answer faster.

### Big O Space Complexity
Since recursion was avoided space complexity is added by the additional variables used in the function. There is one float and three integer variables, although one is a counter to keep track of the number of iterations during testing. This is not needed and could be eliminated. Space complexity should be O(n) where n is the number of variables in the function which is five including the number passed into the function.

### Big O Time Complexity
This appears to be a candidate for recursion, but was done with iteration and avoids the overhead of recursion. The Babylonian method also has less operations to perform then the binary method in the core process. It should perform O(log n) where n is the input number to the function.

---
## Problem #2: Search in a Rotated Sorted Array

### Design
Before it embarks on a binary search the first thing that happens is to check the first, middle and last index position for the target value. If it exist in one of those positions then it returns the respective index. If not it proceeds to partition the input list by iteratively narrowing the partition to find the pivot point. Once the pivot point is found it then performs a binary search.

### Big O Space Complexity
Both finding the pivot point and the binary search require a pointer to the list as well as the first and last pointers. It takes O(n) space to store the list plus the additional variables.

### Big O Time Complexity
Finding the pivot point is similar to a binary search as both begin by halving the list through each iteration and continuing  dividing it in half until we find the pivot point or the target value. Both should operate in O(log n), where n is the input size of the array/list.


---
## Problem #3: Rearrange Array Elements

### Design
Commutative law of addition says it doesn't matter what order you add up numbers as they will always sum to the same answer. So rearranging array elements will always yield the sum of the digits regardless of order. As such it is possible to arrange the digits in multiple ways and always get the sum of the digits.

Divides the list in half and uses a recursive merge sort to create two lists of digits. 

### Big O Space Complexity
Merge sort space complexity is O(n) as it must create a copy of the entire list.

### Big O Time Complexity
Merge sort has a worst case time complexity of O(n log(n)).

---
## Problem #4: Dutch National Flag Problem

### Big O Space Complexity


### Big O Time Complexity


### Design






