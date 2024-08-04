class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, val):
        p = Node(val)
        if self.head is None:
            self.head = p
            return
        p.next = self.head
        self.head = p
        return

    def traversal(self):
        if self.head is None:
            print("LinkedList is Empty")
            return  # Exit the method since the list is empty and there's nothing to traverse
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        return  # Exit the method after completing the traversal

    def deleteAtBeg(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        self.head = self.head.next
        return


# Example usage:
ll = LinkedList()
ll.insertAtBeg(10)
ll.insertAtBeg(20)
ll.traversal()
ll.deleteAtBeg()
ll.traversal()
