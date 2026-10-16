
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add First
    def add_first(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # 2. Add Last
    def add_last(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    # 3. Add Middle (at position)
    def add_middle(self, data, pos):
        if pos < 2:
            print("Invalid middle position")
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    # 4. Delete Middle (at position)
    def delete_middle(self, pos):
        if pos < 2:
            print("Invalid middle position")
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if (temp is None or temp.next is None
                or temp.next.next is None):
            print("Invalid middle position")
            return

        temp.next = temp.next.next
        print("Node deleted")

    # 5. Reverse
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # 6. Display
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
ll = LinkedList()

while True:
    print("\n1. Add First")
    print("2. Add Last")
    print("3. Add Middle")
    print("4. Delete Middle")
    print("5. Reverse")
    print("6. Display")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        ll.add_first(data)

    elif ch == 2:
        data = int(input("Enter data: "))
        ll.add_last(data)

    elif ch == 3:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        ll.add_middle(data, pos)

    elif ch == 4:
        pos = int(input("Enter position: "))
        ll.delete_middle(pos)

    elif ch == 5:
        ll.reverse()
        print("List reversed")

    elif ch == 6:
        ll.display()

    elif ch == 7:
        break

    else:
        print("Invalid choice")
