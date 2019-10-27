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

## Problem #2: Search in a Rotated Sorted Array

## Problem #3: Rearrange Array Elements

## Problem #4: Dutch National Flag Problem







