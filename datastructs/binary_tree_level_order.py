from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    #bfs
    # start from root
    # - if null, return,
    if root is None:
        return result
    # - add left & right to queue
    
    queue = deque()
    queue.append(root)
    
    # while queue is not empty
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    # pop an element, then process queue
    return result



def traverse2(root: TreeNode) -> list:
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        currentLevel = []
        levelSize = len(queue)
        
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
                
        result.append(currentLevel)
    return result;

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def reverse_traverse(root: TreeNode) -> list:
    result = deque()
    
    if root is None:
        return result
    
    dqueue = deque()
    dqueue.append(root)
    
    while dqueue:
        level_size = len(dqueue)
        curr_level = []
        
        for _ in range(level_size):
            currNode: TreeNode = dqueue.popleft()
            
            curr_level.append(currNode.val)
            if currNode.left:
                dqueue.append(currNode.left)
            if currNode.right:
                dqueue.append(currNode.right)
        result.appendleft(curr_level)
        
    return result

def isOdd(num: int) -> bool:
    return False if num % 2 == 0 else True

def zigzag(root: TreeNode) -> list:
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    counter = 0
    
    while queue:
        levelSize = len(queue)
        curr_level = []
        
        for _ in range(levelSize):
            curr_Node: TreeNode = queue.popleft()
            if isOdd(counter):
                curr_level.insert(0, curr_Node.val)
            else:
                curr_level.append(curr_Node.val)

            if curr_Node.left:
                queue.append(curr_Node.left)
            if curr_Node.right:
                queue.append(curr_Node.right)
        
        result.append(curr_level)
        counter += 1
        
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse2(root)))
    print("Level order traversal: " + str(zigzag(root)))
    pass

if __name__ == "__main__":
    main()
