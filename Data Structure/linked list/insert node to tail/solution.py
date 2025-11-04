class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head is not None:
        current = head
        while current.next is not None:
            current = current.next
        current.next = node
    else:
        head = node
    return head

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
