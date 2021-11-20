class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next})'

# create nodes
n3 = Node('pears')
n2 = Node('bananas', n3)
n1 = Node('apples', n2)

# n1 -> n2 -> n3
print(n1.item) # apples
print(n1.next.item) # bananas
print(n1.next.next.item) # pears
print(n1) # ('apples',('bananas',('pears',None)))

# iterate over the nodes
n = n1 # temporary node we advance each iteration
while n is not None: # stop when we run out of nodes
  print(n.item) # prints apples, bananas, pears
  n = n.next # advance the node to the next node

class LinkedList:
    def __init__(self):
    self.root = None
    


    def append(self, element): # add the element to the end
      new_node = Node(element)
        if not self.root = new_node
            self.root - new_node
        else:
            current_node = self.root
            last_node = None
            #loop to the end of the linked list
            while current_node:
                last_node = current_node
                current_node = current_node.next
            
            #Add the new node at the next
            last_node.next = new_node
      print(element)

    def insert(self, element, index): # insert the element at the given index
        if index > self.length():
            raise IndexError(Index out of range: {}'')


    def remove(self, element): # remove the first occurrence of the element

    def get(self, index): # get the element at the given index (starting with 0)

    def find(self, element): # find the first occurrence of the element and return it

    def length(self): # return the length of the list
        current_node = self.root
        length = 0

        while current_node:
            length +=1
            current_node = current_node.next

        return length

    def display(self):
        current_node = self.root

        while current_node:
            print(current_node)
            current_node = current_node.next


nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 0)
print(nums) # [7, 5, 6]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2

node_1 = Node('A')
linked_list = LinkedList()
linked_list.append('A')
linked_list.display()

print(linked_list.lenth())
linked_list.insert('D', 10)