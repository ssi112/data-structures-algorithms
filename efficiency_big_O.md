##Lesson 6 Efficiency

**Input size _sometimes_ affects the run-time of an algorithm**

Especially in a loop if the size determines how many times to run it

Simple Example (_thinking of an "operation" as a single line of Python code - not exactly accurate, but illustrates a point_):

```
def say_hello(n):
	for i in range(n):
		print('hello')
```

Three lines of code to execute if n = 1. As the input increases, the number of lines executed also increases.

As the input increases, the number of lines executed increases by a _proportional amount_. Increasing the input by 1 will cause 1 more line to get run. Increasing the input by 10 will cause 10 more lines to get run. Any change in the input is tied to a consistent, proportional change in the number of lines executed. This type of relationship is called a **linear relationship**.

**Quadratic Rate of Increase**

When the input goes up by a certain amount, the number of operations goes up by the square of that amount. If the input is 2, the number of operations is 2^2 or 4. If the input is 3, the number of operations is 3^2 or 9.

Simple Example:
```
def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")
```

As the input to an algorithm increases, the time required to run the algorithm may also increase, _and different algorithms may increase at different rates_.

The _order_ or _rate of increase_ is important when designing algorithms.

**The rate of increase of an algorithm is also referred to as the order of the algorithm.**

The O in Big O Notation refers to the **o**rder of the rate of increase.

<hr />

#### Big O Notation

Big O notation is used to describe the _order_, or _rate of increase_, in the run-time of an algorithm, in terms of the input size (n).

Written as: **O(n)** n = an algebraic expression using variable n

O(1) = O(0n+1)

O(2n + 2) n = length or amount of data input

In terms of efficiency, while counting lines of code is okay for the basics, the amount of run-time an algorithm requires is based on additional factors. Such as how fast is the processor and how many operations it can perform. Different code can require different opertations for the processor to perform. 

Higher level languages may require fewer lines of code to write, but they typically result in more instructions executing in the background than what is written.

Also, the type of data structure used and how its elements are accessed can influence the efficiency of an algorithm.

O(n^2 + 5)

Input | Number of Operations
----- | -------------------------------
5 | 30
10 | 105
25 | 630
100 | 10,005

In this case, the input has little input on the actual operation. It is the n^2 that has the largest impact. The order or rate of increase is what is _typically_ most important. 

**Approximation**
"Some number of computations must be performed for EACH element in the input."

**Worst / Best Case**

 - Worst Case = upper bounds
 - Best Case = lower bounds
 - Average Case = generalize about the mean

<hr />
**Refer to Jupyter notebook tmp/efficiency_practice.ipynb for examples and some practice problems.**
<hr />

#### Space Complexity

Use Big O Notation as well

How efficient algorithm is in terms of memory usage. Depends on datatypes and internal space requirements. Many highlevel languages wrap their basic datatype with housekeeping functions to make them easier to use and this can lead to them taking more space than expected.

**Basic Datatypes and Storage**

Type | Storage size
-| -
char | 1 byte
bool | 1 byte
int | 4 bytes
float | 4 bytes
double | 8 bytes

**Additional links:**

 - [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
 - [Big O Cheatsheet](https://www.bigocheatsheet.com/)
 


