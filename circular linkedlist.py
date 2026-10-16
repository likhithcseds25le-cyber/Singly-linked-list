
class Node:
    def __init__(self, data):
        self.data = data
        self.next = self

    def length(self):
        return 1


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Length
    def length(self):
        if self.head is None:
            return 0

        count = 1
        temp = self.head

        while temp.next != self.head:
            count += 1
            temp = temp.next

        return count

    # Add First
    def add_first(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        new.next = self.head
        last.next = new
        self.head = new

    # Add Last
    def add_last(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        last.next = new
        new.next = self.head

    # Add Middle (position starts at 1)
    def add_middle(self, data, pos):
        if pos < 2 or pos > self.length():
            print("Invalid middle position")
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new = Node(data)
        new.next = temp.next
        temp.next = new

    # Delete Middle
    def delete_middle(self, pos):
        n = self.length()

        if pos < 2 or pos >= n:
            print("Invalid middle position")
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        temp.next = temp.next.next
        print("Node deleted")

    # Reverse Circular Linked List
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head.next = prev
        self.head = prev

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(HEAD)")


# Main Program
cll = CircularLinkedList()

cll.add_first(10)
cll.add_last("Python")
cll.add_last([1, 2, 3])
cll.add_last({"name": "ABC"})

print("Original Circular Linked List:")
cll.display()
print("Length:", cll.length())

cll.add_middle("Middle", 3)
print("\nAfter Add Middle:")
cll.display()

cll.delete_middle(3)
print("\nAfter Delete Middle:")
cll.display()

cll.reverse()
print("\nAfter Reverse:")
cll.display()
print("Length:", cll.length())
