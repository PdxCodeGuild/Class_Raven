# Stack & Linked List
# In this lab we'll implement some common data structures 
# using a Node class that contains both a value and a reference
#  to another node. These can be chained together.

class Node:
    def __init__(self, item, next=None,):
        self.item = item
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


# Part 1: Stack
# A stack is a FILO (first-in, last-out) data structure that can be visualized like a stack of plates. The only accessible item is the 'top'. There are three operations that can be performed.

# push add a new item to the top of the stack, the previous top item goes underneath it.
# pop removes the item from the top of the stack and returns it, the one below it becomes the new top item.
# peek returns the item at the top of the stack without modifying anything.


class Stack:
  def __init__(self, element):
      self.element = [element]
      self.top = None
      self.node = Node() # encapsulation


    # add a new item to the top of the stack, the previous top item goes underneath it
  def push(self, element):
      x= Node(element)
      self.top = x
      self.next = 
 
       # insert an element at the start (new root)


#   removes the item from the top of the stack and returns it, the one below it becomes the new top item
# remove an element from the start (the root becomes the next node)
  def pop(self):
      return self.element.pop()

#   returns the item at the top of the stack without modifying anything# 
# returns the element on the root node or None if there is no root
  def peek(self):
      return self.element[len(self.element)-1] #totally stole this off the internet - I think this gets the bottom of the stack


# return the number of elements
  def length(self): 
   ...
 

  def __str__(self):
    return f'this stack consists of: {s.length()} items'

s = Stack(1)
s.push(5)
s.push(6)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5

