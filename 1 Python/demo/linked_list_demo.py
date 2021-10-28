class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, element): # add the element to the end
        new_node = Node(element)
        
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            last_node = None
            # loop to the end of the linked list
            while current_node:
                last_node = current_node
                current_node = current_node.next

            # add the new node at the
            last_node.next = new_node

    def insert(self, element, index): # insert the element at the given index
        if index > self.length():
            raise IndexError(f'Index out of range: {index}')

        current_node = self.root
        previous_node = None
        current_index = 0

        while current_node:
            if current_index == index:
                new_node = Node(element)

                previous_node = current_node
                new_node.next = current_node.next
                current_node.next = new_node
          
            current_index += 1
            current_node = current_node.next


    def remove(self, element): # remove the first occurrence of the element
        ...

    def get(self, index): # get the element at the given index (starting with 0)
        current_node = self.root
        current_index = 0

        while current_node:
            if current_index == index:
                return current_node.value

            current_index += 1
            current_node = current_node.next

    def find(self, element): # find the first occurrence of the element and return it
        current_node = self.root
        current_index = 0

        while current_node:
            if current_node.value == element:
                return current_index

            current_index += 1
            current_node = current_node.next

    def length(self): # return the length of the list
        current_node = self.root
        length = 0

        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def display(self):
        current_node = self.root

        while current_node:
            print(current_node, '->', end=' ')
            current_node = current_node.next


linked_list = LinkedList()

linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.append('E')

# print(linked_list.length())

# linked_list.insert('D', 10) # IndexError: Index out of range: 10
# linked_list.insert('K', 1)
# linked_list.insert('P', 0)

# print(linked_list.get(3))
print(linked_list.find('C'))

linked_list.display()