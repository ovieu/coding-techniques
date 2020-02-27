class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head: Node) -> bool:
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def get_cycle_start(head: Node) -> Node:
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return fast
    return None

def get_cycle_len(head: Node) -> int:
    p = head
    len = 0
    while True:
        p = p.next
        len += 1
        if p == head:
            break
    return len

def calculate_cycle_length(head: Node) -> int:
    cycle_meet_point = get_cycle_start(head)
    cycle_len = get_cycle_len(cycle_meet_point)
    return cycle_len

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))
    
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    
    print("cycle len of linkedlist is: " + f'{calculate_cycle_length(head)}')

if __name__ == "__main__":
    main()