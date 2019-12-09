# Udacity's Data Structure and Algorithm Nanodegree

In this course you will learn data structures and algorithms by solving 80+ practice problems. You will begin each course by learning to solve defined problems related to a particular data structure and algorithm. By the end of each course, you would be able to evaluate and assess different data structures and algorithms for any open-ended problem and implement a solution based on your design choices.

Course Outline

**Intro**

* Welcome
* Getting Help and Support
* Python Refresher
* How to Solve Problems
   * A systematic way of approaching and breaking down problems
* Efficiency
   * Understanding the importance of efficiency when working with data structures and algorithms. 
* Project 1 - Unscramble CS Problems
   * Complete five tasks based on a fabricated set of calls and texts exchanged during September 2016
   * Use Python to analyze and answer questions about the texts and calls contained in the dataset
   * Perform run time analysis of your solution and determine its efficiency
  
  
**Data Structures**

* Arrays and Linked Lists
* Build Stacks and Queues
* Apply Recursion to Problems
* Trees - basic trees, traversal & binary search trees
* Maps and Hashing
* Project  2 - Show Me the Data Structures: implement appropriate data structures and corresponding methods
   1. Least Recently Used (LRU) Cache
   2. File Recursion 
   3. Huffman Coding
   4. Active Directory
   5. Blockchain
   6. Union and Intersection
   7. Show Me the Data Structures
         * Include three test cases for each solution
         * In separate text file, write explanation for using given data structure and explain the time and speed efficiency for each solution.
         

**Basic Algorithms**

* Basic Algorithms
* Sorting Algorithms
* Faster Divide & Conquer
* Project 3 - Problems vs. Algorithms
   1. Square Root of an Integer
   2. Search in a Rotated, Sorted Array
   3. Rearrange Array Digits
   4. Dutch National Flag Problem
   5. Autocomplete with Tries
   6. Unsorted Integer Array
   7. Request Routing in a Web Server with a Trie
   

**Advanced Algorithms**

* Greedy Algorithms
* Graph Algorithms
* Dynamic Programming
* A-Star (A*) Algorithm 
* Project 4 - Route Planner **
   * In this project, you will build a route-planning algorithm like the one used in Google Maps to calculate the shortest path between two points on a map. 
  

#### ** Project 4 Notes:

Project #4 notebook requires [plotly](https://plot.ly/python/getting-started/). However, trying to run the notebook locally resulted in this error:

```
ImportError: 
The plotly.plotly module is deprecated,
please install the chart-studio package and use the
chart_studio.plotly module instead.
```

Also just changing `import plotly.plotly as py` in the helpers.py to `import chart_studio.plotly as py` does not work. 

Throws an error `AttributeError: 'Graph' object has no attribute '_node'`

**_Possible Solution_** 

* https://stackoverflow.com/questions/49016596/networkx-digraph-attribute-error-self-succ/49016885#49016885

**Additional Info:**

* https://networkx.github.io/documentation/stable/release/migration_guide_from_1.x_to_2.0.html

**UPDATE NOTE**
It appears registration and an API key are required to use chart_studio.plotly.

## License

The contents of this repository are covered under the [MIT License](mit_license.md)


