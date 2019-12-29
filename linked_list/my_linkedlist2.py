"""
linked list
"""


class Node:
    """a node of linked list"""
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    """traverse and print out the linked list"""
    while node:
        print(node)
        node = node.next


def print_list_backward(cur_node):
    if cur_node == None:
        return
    print_list_backward(cur_node.next)
    print(cur_node)


# a normal node
print(Node("Test Node"))

# an empty node
print(Node())


# define a linked list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3


# print from head to tail
print("=== print in order ===")
print_list(n1)

# print from tail to head
print("=== print in reversed order ===")
print_list_backward(n1)
