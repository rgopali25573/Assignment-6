# Data Structures and Algorithms Implementation

This README provides instructions on how to run the code and summarizes the findings from the implementation and analysis of various data structures and algorithms.

## Part 1: Selection Algorithms

### Code
The implementation for Part 1 can be found in `assignment6_part1.py`.

### How to Run
To run the code for Part 1:

1. Ensure you have Python installed on your system.
2. Navigate to the directory containing `assignment6_part1.py`.
3. Run the script using the command:
   ```
   python assignment6_part1.py
   ```

### Summary of Findings

#### Implementation
- Two selection algorithms were implemented:
  1. Deterministic selection using the Median of Medians approach
  2. Randomized selection using Quickselect
- Both algorithms find the kth smallest element in an array.
- The deterministic algorithm splits the array into groups of five, finds the median of each group, and uses these to determine the overall pivot.
- The randomized algorithm chooses a random pivot at each step.
- Both implementations handle edge cases and use in-place partitioning for space efficiency.

#### Performance Analysis
- Both algorithms have a time complexity of O(n) for selecting the kth smallest element.
- The deterministic algorithm guarantees worst-case linear time O(n).
- The randomized algorithm has an expected time complexity of O(n) but a worst-case of O(n^2).
- Space complexity is O(1) for both algorithms, excluding the recursion stack.

#### Empirical Analysis
- Both algorithms correctly found the kth smallest element in all tests.
- The deterministic algorithm showed consistent performance across different input distributions.
- The randomized algorithm was typically faster for larger arrays but could suffer from skewed partitions.
- The deterministic algorithm's overhead for finding the median of medians was not significant for the input sizes tested.

## Part 2: Data Structures Implementation

### Code
The implementation for Part 2 is split across multiple files:
- `assignment6_part2_arrays_matrices.py`
- `part2_stacksandqueuesusingArray.py`
- `part2_singlyLinkedLists.py`
- `part2_rootedTreesusingLinkedLists.py`

### How to Run
To run each implementation in Part 2:

1. Ensure you have Python installed on your system.
2. Navigate to the directory containing the Python files.
3. Run each script individually using the commands:
   ```
   python assignment6_part2_arrays_matrices.py
   python part2_stacksandqueuesusingArray.py
   python part2_singlyLinkedLists.py
   python part2_rootedTreesusingLinkedLists.py
   ```

### Summary of Findings

#### Performance Analysis
- Arrays: O(1) for access, O(n) for insertion and deletion.
- Stacks and Queues (using arrays): O(1) for push, pop, enqueue, and dequeue operations.
- Linked Lists: O(1) for insertion and deletion at the beginning, O(n) for search or deletion elsewhere.
- Rooted Trees (using linked lists): O(n) for most operations, where n is the number of nodes.

#### Trade-offs Between Arrays and Linked Lists
- Arrays excel in constant-time access when indices are known.
- Linked lists are better for frequent insertions and deletions at any position.
- For stacks and queues, arrays are preferable when size is predetermined, while linked lists are better for dynamic sizing.

#### Practical Applications
- Arrays: Memory management, system-level programming, and scenarios requiring fast element access.
- Queues: Breadth-first search, scheduling systems in operating systems.
- Linked Lists: Dynamic storage management, basis for other data structures like hash tables and graphs.
- Rooted Trees: File systems, organization charts, and hierarchical data representation.

## Conclusion
The choice between arrays and linked lists depends on the specific requirements of the application, such as the need for fast access, frequent insertions/deletions, or dynamic sizing. Understanding these trade-offs is crucial for efficient algorithm and data structure design in various computational scenarios.
