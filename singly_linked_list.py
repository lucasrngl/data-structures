# Singly Linked List implementation

# Singly Linked List complexity: O(n) - The amount of data are increases linearly, so space complexity is O(n)

class Node:

    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    
    # Defining head pointer
    def __init__(self):
        self.head = None

    # Print the linked list
    def print_list(self):
        temp = self.head
        while (temp):
            print(str(temp.item), end=" -> ")
            temp = temp.next

    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, previous_node, new_data):
        if previous_node is None:
            print("The given previous node must in linked list")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    
    def delete_node(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False

print("- Creating a linked list")
linked_list = LinkedList()
print("- Inserting 5 items with various methods")
linked_list.insert_end(1)
linked_list.insert_beginning(2)
linked_list.insert_beginning(3)
linked_list.insert_end(4)
linked_list.insert_after(linked_list.head.next, 5)
print("- Linked list:", end=" ")
linked_list.print_list()
print("\n- Deleting the last node")
linked_list.delete_node(4)
print("- Linked list:", end=" ")
linked_list.print_list()
print("\n- Searching for item 5")
item_to_find = 5
if linked_list.search(item_to_find):
    print(f'- Item {item_to_find} was found')
else:
    print(f'- Item {item_to_find} was not found')
print("- Linked list:", end=" ")
linked_list.print_list()
