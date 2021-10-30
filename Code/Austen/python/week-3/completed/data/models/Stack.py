from data.models import Node
node = Node.node


class stack:
  def __init__(stack):
    stack.top = node('top')
    stack.count = 0

  def push(stack, element):
    element = node(element)
    element.next = stack.top.next
    stack.top.next = element
    stack.count += 1

  def pop(stack):
    try:
      stack.top.next
    except:
      output = 'stack is empty'
    else:
      element = stack.top.next
      stack.top.next = stack.top.next.next
      stack.count -= 1
      output = element.item
    return output

  def peek(stack):
    try:
      stack.top.next.item
    except:
      output = 'stack is empty'
    else:
      output = stack.top.next.item
    return output
