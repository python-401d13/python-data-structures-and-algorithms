# python-data-structures-and-algorithms

# Table of Contents
* Reverse an Array
* Array Shift
* Array Binary Search
* Singly Linked List
* Singly Linked List Insertions
* Singly Linked List kth_from_end
* Merge Linked Lists
* Stacks and Queues
* Queues with Stacks
* First-in, First-out Animal Shelter
* Trees
* Fizz Buzz Tree
* Breadth First Search

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

# Singly Linked List kth_from_end

## Challenge
By TDD write a sinly linked list with a `kth_from_end` method which gets the value of the node kth steps from the end of the linked list.

## Approach & Efficiency
The `kth_from_end` method has Big O time complexity O(n) because finding the length of the linked list takes O(n) time and walking the linked list to find the kth from the end node takes O(n) time too. The `kth_from_end` method Big O space complexity O(1) because no matter how many nodes are in the linked list the same number of variables of the method are made.

## API
New methods to a LinkedList instance are `kth_from_end` which takes an integer k in the range [-l, l) where l is the length of the linked list.

## Solution
![Linked List kth from end whiteboard - 01](/assets/ll-kth-from-end/kth_from_end_00.png)
![Linked List kth from end whiteboard - 02](/assets/ll-kth-from-end/kth_from_end_01.png)
![Linked List kth from end whiteboard - 03](/assets/ll-kth-from-end/kth_from_end_02.png)
![Linked List kth from end whiteboard - 04](/assets/ll-kth-from-end/kth_from_end_03.png)

# Merge Linked Lists

## Challenge
Write a function which takes two linked lists as parameters and returns the two linked lists merged as a zipper. For example, linked lists [2] -> [3] -> [5] and [4] -> [6] -> [7] becomes [2] -> [4] -> [3] -> [6] -> [5] -> [7]. Write the algorithm in Big O space complexity O(1).

## Approach & Efficiency
The Big O time complexity of the algorithm is O(n^2) for a singly linked list. The approach is to walk both linked lists until a null pointer then change pointer, walk both linked lists again but until a null pointer minus one step, then again until a null pointer minus two steps, and so on until no steps are taken. The algorithm also handled cases where one or both linked lists are empty.

## API
The way to test the code is through the pytest module of Python. The algorithm and tests are written in Python. The `merge_lists` function written is not an instance method of the LinkedList class so must be imported separately from the LinkedList class for use.

## Solution
![Merge Linked Lists - 01](/assets/ll-merge/ll_merge_01.png)
![Merge Linked Lists - 02](/assets/ll-merge/ll_merge_02.png)
![Merge Linked Lists - 03](/assets/ll-merge/ll_merge_03.png)

# Stacks and Queues
Stacks are a "first in last out" data structure when storing data. Queues are a "first in first out" data strucutre when storing data.

## Challenge
Write methods to add, remove and see the head of a stack and a queue.

## Approach & Efficiency
In all cases adding, removing and seeing the head of a stack or a queue can be done in O(1).

## API
Python classes are used to model Stack and Queue data structures with methods. TDD was used to test the instance methods and the tests can be run with pytest to see the validity of the instance methods.

# Queues with Stacks
Make a queue data structure interface made with two stack data structure instances.

## Challenge
Write queue interface methods enqueue and dequeue.

## Approach & Efficiency
To enqueue a value to the pseudo queue all values are popped into a second stack, the value is pushed to the top of the second stack and then all values are popped from the second stack back into the first stack. To dequeue a value from the pseudo queue the top of the first stack is popped off.

## API
The Pseudo Queue instance methods are enqueue which takes a value to add to the front of the queue and dequeue which removes a value from the front of the queue.

## Solution
![Queues with Stacks](/assets/queues_with_stacks.png)

# First-in, First-out Animal Shelter
Write a first-in first-out AnimalShelter class which has Cats and Dogs.

## Challenge
Write queue interface methods enqueue and dequeue. Enqueue takes an Animal to enqueue and returns nothing. Dequeue takes an Animal preference to let go and returns the animal if in the shelter.

## Approach & Efficiency
The AnimalShelter class is implemented with two Stacks. Enqueuing to the AnimalShelter takes Big O time O(n) and Big O space O(1). Dequeing from the AnimalShelter takes Big O time O(n) and Big O space O(1).

## API
The AnimalShelter is a Queue data structure and so has instance methods enqueue and dequeue though peek is not included because the Stacks are used to peek.

## Solution
![First-in, First-out Animal Shelter - 01](/assets/fifo-animal-shelter/fifo-animal-shelter-01.png)
![First-in, First-out Animal Shelter - 02](/assets/fifo-animal-shelter/fifo-animal-shelter-02.png)

# Trees
Binary Trees and Binary Search Trees are a data structure often used in software. A Binary Tree or Binary Search Tree is an example of what a file system may look like. For balanced Binary Search Trees search time is O(log n).

## Challenge
Write instance methods of a Binary Tree `pre-order`, `in-order` and `post-order` which show a list of the tree values in these traversal orders. Write instance methods of a Binary Search Tree `add` and `contains` which update and read a Binary Search Tree for a value in time O(log n).

## Approach & Efficiency
API methods of instances of a Binary Tree and a Binary Search Tree `pre-order`, `in-order` and `post-order` take Big O time O(n) and space O(1). The API method of instances of a Binary Search Tree `add` and `contains` take Big O time O(log n) and space O(1).

## API
The API instance methods for a Binary Tree and Binary Search Tree are `pre-order`, `in-order` and `post-order`. The API instance methods for a Binary Search Tree are `add` and `contains`

# Fizz Buzz Tree
Write a function fizzbuzz_tree which takes a tree and returns a new tree with values fizzbuzzed.

## Challenge
WWrite a function fizzbuzz_tree which takes a tree and returns a new tree with values fizzbuzzed.

## Approach & Efficiency
The approach used was to write a helper function `fizzbuzz_node` which takes a node and returns a fizzbuzzed node. Left and right nodes are apart of the returned node. The tree given to `fizzbuzz_tree` is made with nodes by the recursive function `fizzbuzz_node` and the return of the root node in the `fizzbuzz_tree` definition is used to make a new tree which is returned from the `fizzbuzz_tree` function.

## API
The user facing function is `fizzbuzz_tree`. The developer facing helper function `fizzbuzz_node` is used to fizzbuzz the values of the tree given to the `fizzbuzz_tree` function.

## Solution
![Fizz Buzz Tree](/assets/fizz-buzz-tree.png)

# Breadth First Search

## Challenge
Write a method for a Binary Tree which returns a list of values in the tree in breadth-first order.

## Approach & Efficiency
The approach is use a Queue to enqueue nodes of a Binary Tree and for each node in the Queue add the node's value to a list which is to be returned. The approach taken has both time and space efficiency O(N).

## API
The new `breadth_first_search` method of the BinaryTree class can be used with no arguments to get a list of the tree's values in breadth-first order.

## Solution
![Breadth First Search - 01](/assets/breadth_first_search/breadth_first_search_01.png)
![Breadth First Search - 02](/assets/breadth_first_search/breadth_first_search_02.png)
