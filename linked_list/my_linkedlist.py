"""
singly-linked list
"""

class ListNode(object):
    def __init__(self):
        self.val = None
        self.next_node = None

class LinkedList_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        """add a new node pointed to previous node"""
        node = ListNode()
        node.val = data
        node.next_node = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
            while node:
                if not isinstance(node.val, type(None)):
                    if node.next_node:
                        print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next_node.val)
                    else:
                        print('\nnode: ', node, ' value: ', node.val, ' next: ', "NULL")
                else:
                    print('\nnode: ', node, ' value: ', "NULL", ' next: ', "NULL")

                node = node.next_node



def main():
    print("===Singly-Linked List===")
    mylnklist = LinkedList_handle()
    n1 = ListNode()
    mylnklist.add(1)

    n2 = ListNode()
    mylnklist.add(2)

    n3 = ListNode()
    mylnklist.add(3)

    mylnklist.print_ListNode(mylnklist.cur_node)


if __name__ == "__main__":
    main()

