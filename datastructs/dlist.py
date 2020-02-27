from typing import List
from stack import Stack

class DNode:
    def __init__(self, item):
       self.item = item
       self.next = None
       self.prev = None

class Dlist:
    def __init__(self):
        self.senNodeFirst =  self.createNode("")
        self.senNodeLast = self.createNode("")
        self.senNodeFirst.next = self.senNodeLast
        self.senNodeLast.prev = self.senNodeFirst
        self.senNodeFirst.prev = self.senNodeLast.next = None

    def addFirst(self, item):
        new_item = self.createNode(item)
        self.insertAfter(self.senNodeFirst, new_item)

    def addLast(self, item):
        new_item = self.createNode(item)
        self.insertBefore(self.senNodeLast, new_item)

    def isEmpty(self):
        return (self.senNodeFirst.next == self.senNodeLast)

    def createNode(self, item):
        new_node = DNode(item)
        return new_node

    def insertAfter(self, currNode: DNode, item: DNode):
        item.prev = currNode
        item.next = currNode.next
        item.next.prev = item
        item.prev.next = item

    def insertBefore(self, currNode: DNode, item: DNode):
        item.next = currNode
        item.prev = currNode.prev
        item.next.prev = item
        item.prev.next = item

    def printList(self):
        p = self.senNodeFirst.next
        while (p != self.senNodeLast):
            print(p.item)
            p = p.next


def threeSum(nums: List[int]) -> List[List[int]]:
    num_set = set(nums)
    result = []
    for num in nums:
        for i in range(len(nums)):
            if (num == nums[i]):
                continue
            target = - (num + nums[i])
            if target in num_set:
                part_result = [num, nums[i], target]
        part_result.sort()
        if (part_result not in result):
            result.append(part_result)
    return result

def reverseString(input_str):
   stack = []
   for ch in input_str:
       stack.append(ch)


if __name__ == "__main__":
    list = Dlist()
    for i in range(10):
        list.addFirst(i)
    list.printList()
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum(nums)
    print(result)

