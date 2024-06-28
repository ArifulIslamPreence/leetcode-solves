from collections import deque, defaultdict

# Tree node class

class Node:    
    def __init__(self, key):
        self.data = key  # data of the node
        self.hd = float('inf')  # horizontal distance of the node
        self.left = None  # left reference
        self.right = None  # right reference

# Method that prints the bottom view.

def bottomView (root):
    if root is None:
        return

    # Initialize a variable 'hd' with 0 for the root element.
    hd = 0

    # Dictionary to store key-value pairs sorted on key value
    m = defaultdict(int)

    # Queue to store tree nodes in level order traversal
    q = deque()

    # Assign initialized horizontal distance value to the root node and add it to the queue.
    root.hd = hd
    q.append(root)

    # Loop until the queue is empty (standard level order loop)
    while q:
        temp = q.popleft()

        # Extract the horizontal distance value from the dequeued tree node.
        hd = temp.hd

        # Put the dequeued tree node to the dictionary with key as horizontal distance.
        # Every time we find a node having the same horizontal distance, we need to replace the data in the dictionary.
        m[hd] = temp.data

        # If the dequeued node has a left child, add it to the queue with a horizontal distance hd-1.
        if temp.left:
            temp.left.hd = hd - 1
            q.append(temp.left)

        # If the dequeued node has a right child, add it to the queue with a horizontal distance hd+1.
        if temp.right:
            temp.right.hd = hd + 1
            q.append(temp.right)

    # Traverse the dictionary elements and print the values.
    for key in sorted(m):
        print(m[key], end=" ")

# Driver Code
if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print("Bottom view of the given binary tree:")
    bottomView(root)