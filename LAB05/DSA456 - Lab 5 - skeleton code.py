# Name : Danny Rai
# student id: 147986236

#Part A
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.is_empty(): self.head = node
        else:
            temp = self.head
            while temp.next:  temp = temp.next
            temp.next = node

    def insert_after(self, target, data):
        if target is None: return False
        node = Node(data, target.next)
        target.next = node
        return True

    def delete(self, target):
        if self.is_empty(): return False
        if self.head == target:
            self.head = self.head.next
            return True
        temp = self.head
        while temp.next and temp.next != target: temp = temp.next

        if temp.next == target:
            temp.next = target.next
            return True
        return False

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data: return temp
            temp = temp.next
        return None

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def to_list(self) :
        items = []
        temp = self.head
        while temp:
            items.append(temp.data)
            temp = temp.next
        return items

    def print(self) :
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("None")


linked_list = SinglyLinkedList()
linked_list.append(15)       # add 15 at the end of the list 
linked_list.append(9)        # add 9 at the end of the list
linked_list.prepend(4)       # add 4 at the start of the list so the order will be: 4 → 15 → 3
linked_list.print()          # prints 4 15 9 None which are teh values in the list
print(linked_list.size())    # prints 3 wchich is the number of used nodes which don't have the value None
node = linked_list.search(9) # new node from the list with value 9
linked_list.insert_after(node, 1)   # inset after the target node
linked_list.print()          # prints 4 15 9 1 None 
linked_list.delete(node)     # delete the node
linked_list.print()          # prints 4 15 1 None

#Part B
"""
-> __intit__() function only set the header pionter so T(n) = 1 = O(1)
    is_empty() functions only check the head pointer so T(n) = 1 = O(1)
    prepend() just adds a node at the start so T(n) = 1 = O(1)
    insert_after() only performs a check for a target then adds a node after so T(n) = 1 = O(1)
    search() function which visits all nodes so T(n) = n = O(n)
    size() function which visits all nodes so T(n) = n = O(n)
    to_lis() function which visits all nodes so T(n) = n = O(n)
    rint() function which visits all nodes so T(n) = n = O(n)
    append() traverses the whole list to reach the end and then adds a node so T(n) = n = O(n)
"""