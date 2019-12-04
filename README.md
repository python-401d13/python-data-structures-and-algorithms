# python-data-structures-and-algorithms

# Table of Contents
* Reverse an Array
* Array Shift
* Array Binary Search

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

[Code Solution](https://github.com/python-401d13/python-data-structures-and-algorithms/pull/2)
