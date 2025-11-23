# Name : Danny Rai
# student id: 147986236
class Node:
    def __init__(self, value=None, nxt=None, prev=None) -> None:
        self.value = value
        self.next = nxt
        self.previous = prev

    def get_data(self):
        return self.value


class LinkedList:
    def __init__(self, front=None, back=None) -> None:
        self.start = None
        self.end = None
        self.count = 0

    # Show all values in the list
    def show(self):
        curr = self.start
        items = []
        while curr:
            items.append(curr.value)
            curr = curr.next
        print(" <-> ".join(map(str, items)) if items else "Empty List")

    # Return the first value
    def get_front(self):
        return None if self.count == 0 else self.start.value

    # Return the last value
    def get_back(self):
        return None if self.count == 0 else self.end.value

    # Insert at the front
    def insert_front(self, data):
        new_node = Node(data)
        if self.count == 0:
            self.start = new_node
            self.end = new_node
        else:
            new_node.next = self.start
            self.start.previous = new_node
            self.start = new_node
        self.count += 1

    # Insert at the back
    def insert_back(self, data):
        new_node = Node(data)
        if self.count == 0:
            self.start = new_node
            self.end = new_node
        else:
            new_node.previous = self.end
            self.end.next = new_node
            self.end = new_node
        self.count += 1

    # Insert in sorted order
    def insert(self, data):
        new_node = Node(data)
        if self.count == 0:
            self.start = new_node
            self.end = new_node
        elif data < self.start.value:
            self.insert_front(data)
        elif data > self.end.value:
            self.insert_back(data)
        else:
            curr = self.start
            while curr and curr.value < data:
                curr = curr.next
            before = curr.previous
            new_node.previous = before
            new_node.next = curr
            before.next = new_node
            curr.previous = new_node
            self.count += 1

    # Remove the first matching value
    def remove(self, data):
        curr = self.start
        while curr:
            if curr.value == data:
                if curr == self.start:
                    self.start = curr.next
                    if self.start:
                        self.start.previous = None
                elif curr == self.end:
                    self.end = curr.previous
                    if self.end:
                        self.end.next = None
                else:
                    curr.previous.next = curr.next
                    curr.next.previous = curr.previous
                self.count -= 1
                return True
            curr = curr.next
        return False

    # Check if a value is in the list
    def is_present(self, data):
        curr = self.start
        while curr:
            if curr.value == data:
                return True
            curr = curr.next
        return False

    # Return size
    def __len__(self):
        return self.count


if __name__ == "__main__":
    dissplay = LinkedList()
    dissplay.insert(5)
    dissplay.insert(3)
    dissplay.insert(7)
    dissplay.show()
    dissplay.remove(5)
    dissplay.show()
    print(dissplay.is_present(7))
    print(dissplay.get_front())
    print(dissplay.get_back())
    print(len(dissplay))
