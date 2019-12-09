# python-data-structures-and-algorithms

# Table of Contents
* Reverse an Array
* Array Shift
* Array Binary Search
* Singly Linked List
* Singly Linked List Insertions

# Reverse an Array

## Challenge
Define a function which takes an arary and returns an array with elements reversed.

## Approach & Efficiency
The approach taken was to sort the array in-place without creating a new array. The efficiency of the approach is O(N) since every element in the array is seen.

## Solution
![Solution](/assets/array-reverse.png)

# Array Shift

## Challenge
Define a function which takes an array and an element and returns the same array with the element inserted at the middle.

## Approach & Efficiency
The approach was to find the index of the middle of the array, slice the array around the middle index, the concatenate a new array with the new element between the left and right slice of the array.

## Solution
![Solution](/assets/array-shift.png)

[Code Solution](https://github.com/python-401d13/python-data-structures-and-algorithms/pull/2)

# Array Binary Search

## Challenge
Write a function which takes a sorted list and a value and returns the index of the value in the list or -1 otherwise.

## Approach & Efficiency
Without enough time to write through the O(log N) binary search the written solution is an iterative solution which run in O(N) time.

## Solution
![Binary Search Whiteboard - 01](/assets/array_binary_search/00)
![Binary Search Whiteboard - 02](/assets/array_binary_search/01)
![Binary Search Whiteboard - 03](/assets/array_binary_search/02)

![Binary Search Iteration Whiteboard - 01](/assets/array_binary_search/03)
![Binary Search Iteration Whiteboard - 02](/assets/array_binary_search/04)
![Binary Search Iteration Whiteboard - 03](/assets/array_binary_search/05)

[Code Solution](https://github.com/python-401d13/python-data-structures-and-algorithms/pull/3)

# Singly Linked List

## Challenge
By TDD write a Linked List data structure with insert and includes methods, and a method for seeing all values in the linked list. Write the Linked List and related Nodes in Python classes. Methods should follow the Single Responsibility Principle.

## Approach & Efficiency
Linked Lists are good data structures for adding or removing values quickly from a grouping of values. The Big O time complexity of inserting a value into a linked list is O(1) because the same number of step are taken regardless of the size of the linked list. The Big O time complexity of checking if a linked list includes a value is O(n) because in the worst case of a value not being in the linked list all nodes of the linked list are walked through. Similarly, seeing a grouping of all values in the linked list together take Big O time complexity O(n) because every node in the linked list is checked.

## API
A coder using the linked list class data structure will be able to use insert and includes instance methods. The coder can also see all values of the linked list by checking the string state of a linked list class instance. The insert method of a linked list class instance adds a value to the head of the linked list, when walking the linked list afterwords the value will be the first seen. The includes method of a linked list class instance checks a linked list for a value, if the value is in the linked list the method will return True, otherwise False.

# Singly Linked List Insertions

## Challenge
By TDD write a singly linked list with an `append` method which adds a new value to the end of the linked list, an `insert_before` method which adds a value before another value, and an `insert_after` method which adds a value after another value.

## Approach & Efficiency
The `append` method has O(n) time as the singly linked list needs to be walked to the end to append a value. The `insert_before` method has O(n) time as the singly linked list may need to walk the whole linked list trying to find the old value to insert before. The `insert_after` method has O(n) time as the singly linked list may need to walk the whole linked list trying to find the old value to insert after.

## API
New methods to a LinkedList instance are `append` which appends a value at the end of a linked list, `insert_before` which inserts a new value before an old value and `insert_after` which inserts a new value after an old value.

## Solution
![Linked List insertions Whiteboard - 01](/assets/ll-insertions/ll-insertions-00.png)
![Linked List insertions Whiteboard - 02](/assets/ll-insertions/ll-insertions-01.png)
![Linked List insertions Whiteboard - 03](/assets/ll-insertions/ll-insertions-02.png)
