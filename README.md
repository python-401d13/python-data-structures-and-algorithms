# python-data-structures-and-algorithms

# Table of Contents
* Reverse an Array
* Array Shift

# Reverse an Array
Define a function which takes an array and returns an array with elements reversed.

## Challenge
Define a function which takes an arary and returns an array with elements reversed.

## Approach & Efficiency
The approach taken was to sort the array in-place without creating a new array. The efficiency of the approach is O(N) since every element in the array is seen.

## Solution
![Solution](/assets/array-reverse.png)

# Array Shift
Define a function which takes an array and an element and returns the same array with the element inserted at the middle.

## Challenge
Define a function which takes an array and an element and returns the same array with the element inserted at the middle.

## Approach & Efficiency
The approach was to find the index of the middle of the array, slice the array around the middle index, the concatenate a new array with the new element between the left and right slice of the array.

## Solution
![Solution](/assets/array-shift.png)

[Code Solution](https://github.com/python-401d13/python-data-structures-and-algorithms/pull/2)
