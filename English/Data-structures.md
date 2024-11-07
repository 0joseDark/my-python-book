Data structures are ways of organizing and storing data to allow efficient access and modification. They form the backbone of how data is managed and manipulated in programming and computer science. Here are some common data structures, their explanations, and examples:

### 1. **Arrays (or Lists)**
   - **Description**: An array is a collection of items stored at contiguous memory locations. Arrays store multiple items of the same data type and can be accessed by an index.
   - **Example**:
     ```python
     # Python example of an array (list)
     fruits = ["apple", "banana", "cherry"]
     print(fruits[1])  # Output: banana
     ```

### 2. **Linked Lists**
   - **Description**: A linked list is a sequence of nodes where each node contains data and a reference (or link) to the next node. It allows efficient insertion and deletion of elements.
   - **Example**:
     ```python
     # Simple Python example of a singly linked list
     class Node:
         def __init__(self, data):
             self.data = data
             self.next = None

     # Creating nodes and linking them
     node1 = Node("apple")
     node2 = Node("banana")
     node1.next = node2  # link node1 to node2
     print(node1.data, "->", node1.next.data)  # Output: apple -> banana
     ```

### 3. **Stacks**
   - **Description**: A stack is a LIFO (Last-In, First-Out) structure where elements are added (pushed) and removed (popped) from the top. Commonly used for backtracking and in recursive algorithms.
   - **Example**:
     ```python
     # Python example of a stack using a list
     stack = []
     stack.append("apple")  # push
     stack.append("banana")
     print(stack.pop())  # Output: banana (popped)
     ```

### 4. **Queues**
   - **Description**: A queue is a FIFO (First-In, First-Out) structure where elements are added at the back (enqueue) and removed from the front (dequeue). It's useful for managing tasks in order.
   - **Example**:
     ```python
     # Python example of a queue using collections.deque
     from collections import deque
     queue = deque(["apple", "banana"])
     queue.append("cherry")  # enqueue
     print(queue.popleft())  # Output: apple (dequeued)
     ```

### 5. **Hash Tables (Dictionaries in Python)**
   - **Description**: A hash table stores key-value pairs, where each key is unique and mapped to a specific value. This structure enables fast lookups.
   - **Example**:
     ```python
     # Python example of a hash table (dictionary)
     fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
     print(fruit_colors["banana"])  # Output: yellow
     ```

### 6. **Trees**
   - **Description**: A tree is a hierarchical structure consisting of nodes, with a root node and child nodes forming branches. Trees are used in representing structured data like file systems or hierarchies.
   - **Example** (Binary Tree):
     ```python
     # Simple binary tree in Python
     class TreeNode:
         def __init__(self, data):
             self.data = data
             self.left = None
             self.right = None

     root = TreeNode(1)
     root.left = TreeNode(2)
     root.right = TreeNode(3)
     print(root.data, root.left.data, root.right.data)  # Output: 1 2 3
     ```

### 7. **Graphs**
   - **Description**: A graph is a set of nodes (vertices) connected by edges. Graphs can be directed or undirected, representing various networks, such as social networks or city maps.
   - **Example**:
     ```python
     # Python example of a simple graph using a dictionary
     graph = {
         "A": ["B", "C"],
         "B": ["A", "D"],
         "C": ["A", "D"],
         "D": ["B", "C"]
     }
     print(graph["A"])  # Output: ['B', 'C']
     ```

Each of these data structures has different use cases depending on the requirements of the program, such as the need for quick access, ordered elements, or relationships between data points.
