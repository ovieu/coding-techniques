from typing import List, Any


def intersect(num1, num2):
    result = []
    for i in num1:
        for j in num2:
           if (i == j):
             result.add(i)
    return result;

def intersect2(num1, num2):
    result = []
    num1_set = set(num1)
    for nam in num2:
        if nam in num1_set:
            result.append(nam)
    return result

def intersect2(num1, num2):
    return list(set(num1) & set(num2))


class LinkedList:
    class Node:
        def __init__(self, value, next, prev):
            self.value = value
            self.prev = prev
            self.next = next

        def __str__(self):
            return '{' \
                   '' \
                   '}'

