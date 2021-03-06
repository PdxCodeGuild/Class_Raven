"""
Lee Colburn
Evening Bootcamp - PDX Code Guild
Optional Lab - Stack and Linked List 
"""
# In this lab we'll implement some common data structures using a Node class that contains both a value and a reference to another node. 
# These can be chained together.

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next})'

# create nodes
n3 = Node('pears')
n2 = Node('bananas', n3)
n1 = Node('apples', n2)

# n1 -> n2 -> n3
'''print(n1.item) # apples
print(n1.next.item) # bananas
print(n1.next.next.item) # pears
print(n1) # ('apples',('bananas',('pears',None)))'''

# iterate over the nodes
n = n1 # temporary node we advance each iteration
while n is not None: # stop when we run out of nodes
  print(n.item) # prints apples, bananas, pears
  n = n.next # advance the node to the next node


###################### Part 1: Stack #########################
# A stack is a FILO (first-in, last-out) data structure that can be visualized like a stack of plates. 
# The only accessible item is the 'top'. 

### There are three operations that can be performed:
# push add a new item to the top of the stack, the previous top item goes underneath it.
# pop removes the item from the top of the stack and returns it, the one below it becomes the new top item.
# peek returns the item at the top of the stack without modifying anything.

# Stub:
class Stack:
  def __init__(self, element, top=False):
    self.top = top
    self.element = element

  def push(self, element): # insert an element at the start (new root)  

    return

  def pop(self): # remove an element from the start (the root becomes the next node)

    return

  def peek(self): # returns the element on the root node or None if there is no root

    return

  def length(self): # return the number of elements
    return 2

  def __str__(self):
    return f'({self.item}, {self.top})'

s = Stack()
s.push(5)
s.push(6)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5

######################### Part 2: Linked List #########################
# A linked list is similar to the built-in list in Python, and provides methods for adding and removing elements.

# append - adds a new element to the end of a list
# insert - inserts a new element at a given index
# remove - remove the first occurrence of the element
# get - get the element at the given index (starting with 0)
# find - find the first occurrence of the element and return it
# length - return the length of the list

# Stub:
class LinkedList:
  def __init__(self):
    self.root = None
  def append(element): # add the element to the end
    ...
  def insert(element, index): # insert the element at the given index
    ...
  def remove(element): # remove the first occurrence of the element
    ...
  def get(index): # get the element at the given index (starting with 0)
    ...
  def find(element): # find the first occurrence of the element and return it
    ...
  def length(self): # return the length of the list
    ...

'''nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 0)
print(nums) # [7, 5, 6]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2'''
