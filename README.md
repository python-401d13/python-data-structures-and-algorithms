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
* Find Maximum Binary Tree
* Hashtable
* Repeated Word
* Tree Intersection
* Left Join
* Graph
* Breadth First Graph
* Get Edge
* Depth First

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

# Find Maximum Binary Tree

## Challenge
Write an instance method `find_maximum_value` for a Binary Tree which finds the maximum value of a Binary Tree of numbers.

## Approach & Efficiency
The approach used is a depth-first search which takes a root node as an argument to the instance method call. The depth-first search is done in the pre-order way. Maximum values of depth searches are returns and evaluated for the current node, the left of the current node and the right of the current node. The Big O time efficiency is O(n) where n is the number of nodes in the tree. The Big O space efficiency is O(h) where h is the height of the tree and so the maximum height of the call-stack.

## API
The `find_maximum_value` instance method takes a root node as a parameter to find maximum values from by pre-order depth-first search.

## Solution
![Find Maximum Binary Tree](/assets/find-maximum-binary-tree.png)

# Hashtable
Hashtables are a common data structure which can read and write in time O(1). Hashtables are used to make programming dictionaries. Like a natural language dictionary, when a word has more than one definition the reader must step through each definition until finding the definition they're looking for or exit after reading all definitions.

## Challenge
Write a Hashtable class in Python. Test all methods of a Hashtable data structure. These methods are add, get, contains and hash.

## Approach & Efficiency
A hashtable without collisions in a bucket adds, gets and checks for containment in time O(1). A hashtable with collisions in a bucket does these methods in time relative to the number of key-value pairs in the bucket. Hashtables are said to have "amortized time O(1)".

## API
The API for a hashtable are methods add, get, contains and hash. Add is a method which takes a key-value pair and adds the pair at the correct index of the hashtable. Get returns a value given a key of a hashtable or raises an exception otherwise. Contains checks if a hashtable has a key. Finally hash takes a key and finds the index of the hashtable to keep the key-value pair.

# Repeated Word
Many pieces of writing whether they're phrases, sentences, paragraphs or otherwise have mnay words repeated. One of the most common words used in English is 'the'. Natural language often needs words repeated in writing to be readable.

## Challenge
Write a function named `repeated_words` which takes a lengthy string and returns the first repeated word from the string or null if there are no repeated words.

## Approach & Efficiency
The function written takes time O(N) and space O(N) to run where N is the number of unique words in the lengthy string. Because the non-string value None is returned from the function when the lengthy string has no repeated words, dictionary reads can happen in O(1) time keeping function run time to O(N). If all keys were read in the dictionary (kept holding all words seen so far in the lengthy string) the run time of the function would become O(N^2).

## API
The only function written is `repeated_words` which takes a lengthy string to be checked for the first repeated word. The first repeated word is returned from the function or None if no repeated words are in the lenghty string. A known limitation of the function is plurals are seen as different words.

## Solution
![Repeated word whiteboard](/assets/repeated_word.png)

# Tree Intersection
Binary Trees can be in many shapes but are most useful when balanced. Walking Binary Trees in depth-first order is done the same as walking Binary Search Trees which can be done in pre-order, in-order or post-order. Binary Trees, like Binary Search Trees, can also be walked in depth-first order.

## Challenge
Write a function named `tree_intersection` which takes two trees and returns a set with the intersection of values in both trees. Write tests for the function.

## Approach & Efficiency
The challenge is broken into two functions: `tree_intersection` and `walk`. The `tree_intersection` is the main function which uses the `walk` function as a helper for walking a Binary Tree recursively. At each recursive step of the walk a value is either added to a union set of the two trees in `tree_intersection` or added to an intersection set of the two trees. Time and space complexity of `tree_intersection` is O(1). Time and space complexity of `walk` is O(N) where N is the number of nodes in a tree.

## API
There are two functions: `tree_intersection` and `walk`. The first function, `tree_intersection`, is public. The second function, `walk`, is protected.

## Solution
![Tree Intersection](/assets/tree_intersection.png)

# Left Join
Merging two collections together is a common task. The union and intersection of two collections are common ways to look at to analyze the merge of two collections. In the field of software, a left join of two collections is a collection with all values from the left collection which includes the intersection of the left and right collections.

## Challenge
Write a function which takes two dictionaries, key-values pairs of words and synonyms and key-value pairs of words and antonyms. From the function return a new data structure which is the left join of the synonyms dictionary to the antonyms dictionary.

## Approach & Efficiency
The solution used is to create an empty dictionary at the start of the function which will be returned at the end of the function. Walk through the dictionary of synonyms adding keys to a list of values for all key-value pairs. For each key in the dictionary of synonyms also add the value of the key in the dictionary of antonyms or None otherwise. The solutions take time O(N) and space O(N) where N is the number of keys in the dictionary of synonyms.

## API
There's one function created for the solution which is `left_join`. The function takes two dictionaries as parameters. What's returned from the function is a new dictionary which is the left join of the first and second parameter dictionaries.

## Solution
![Left Join whiteboard](/assets/left-join.png)

# Graph
Graphs are a common data structure. They can be used to model networks of friends, airports or other hubs. The graph data structure can be used to imagine the web.

## Challenge
Write a Graph class in Python along with helper classes. Add methods `add_node`, `add_edge`, `get_nodes`, `get_neighbors` and `size` to the Graph class.

## Approach & Efficiency
A graph can be modeled similar to a hashtable with a dictionary, doing so makes an adjacency list. Each key of the adjacency list is a node in the graph. Neighbors of a node are kept in a collection mapped to by the key in the adjacency list.

## API
Classes added are `Graph` and `Vertex`. There are no methods of the `Vertex` class. Methods of the `Graph` class are `add_node`, `add_edge`, `get_nodes`, `get_neighbors` and `size`.

# Breadth First Graph
There are two common ways to walk a graph: breadth first and depth first. Walking a graph breadth first is similar to walking a tree breadth first. When working with a tree the root is often taken as where to walk from breadth first, when working with a graph a given node is taken as where to walk from breadth first.

## Challenge
As a whiteboard interview problem find a solution to walking a graph breadth first. Write tests for the solution too. Find the Big O time and space of walking a graph breadth first.

## Apprach & Efficiency
The approach taken to solving the problem is using a queue which holds onto the neighbors a current vertex. While the queue is not empty continue dequeueing vertices and checkings neighbors of the vertex. If a vertex is in a list of seen vertices don't add the vertex's neighbors to the vertices list and don't add the vertex to the vertices list, otherwise do both. The Big O time for breadth first search is O(N^2) and the Big O space is O(N).

## API
The Graph class is extended with the BreadthFirstGraph class. The BreadthFirstGraph has a new method named `breadth_first`. The methods takes in a vertex and gives out a list of vertices seen in a breadth first walk starting from the starting vertex.

## Solution
![Breadth First Graph](/assets/breadth_first_graph.png)

# Get Edge
Walking graph is a common task. Seeing if a walk through a graph and the cost of the walk goes with walking a graph.

## Challenege
Write a function `get_edge` which takes in a graph and a list of values. The function should give out a boolean saying whether a walk between the values as nodes can happen and the cost of the walk. If the walk can't happen the cost is $0.

## Approach & Efficiency
The list of values taken into the function is a could-be list of vertex values. The first step is to get a list of nodes whose values are the values from the list taken into the function. From the list of nodes neighbors are checked to see if the walk can happen and what the cost of the walk is. The Big O time is O(N^2) and the Big O space is O(N) where N is the number of vertices in the graph and the number of values in the list taken into the function.

## API
The new function is `get_edge` whose parameters are a graph and a list of could-be graph vertex values. What's given out from the function is a boolean telling whether the walk between each list value taken into the function can happen in order and what the cost of the walk is. When the walk can't happen a false boolean along with $0 in a string is given out from the function.

## Solution
![Get Edge](/assets/get_edge.png)

# Depth First
Given a graph there are two common ways to walk through the graph. Depth first if one of these common walks. Given a starting vertex each path which can be walked starting from the starting vertex is walked. Each vertex seen is tracked and not recycled in a future walk.

## Challenge
Write a function which takes a graph as an adjacency list and a starting vertex. From the function return a collection of vertices in depth first pre-order from a walk of the graph starting at the starting vertex.

## Approach & Efficiency
The approach taken was to define two functions `depth_first` and `walk`. The `depth_first` function is the entrypoint where edge cases of the graph and starting vertex are handled. The starting empty collection of vertices in the graph is made here too. The `walk` function is used for the pre-order depth first walk of the graph starting from the starting vertex.

| O | time | space |
| --- | --- | --- |
| depth_first | O(1) | O(1) |
| walk | O(N) | O(N) |

Where N is the number of vertices in the graph.

## API
New functions are `depth_first` which takes a graph and a vertex and a return a set of the graph vertices seen in depth first pre-order starting from the staring vertex. The other function is `walk` which takes a graph, a starting vertex and a set. There's no return from the `walk` function. The set is added to in-place through the pre-order depth first walk of the graph starting from the starting vertex.

## Solution
![Depth First](/assets/depth_first.png)
