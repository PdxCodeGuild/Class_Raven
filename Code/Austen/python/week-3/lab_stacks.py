from data.models import Node, Stack
node = Node.node
stack = Stack.stack


def nodes():
  node3 = node('pears')
  node2 = node('bananas', node3)
  node1 = node('apples', node2)
  next = node1
  while next is not None:
    print()
    print(next.item)
    print()
    next = next.next


def stacks():
  data = stack()
  data.push('apples')
  data.push('bananas')
  print(data.peek())
  print(data.count)
  popped = data.pop()
  print(popped)
  print(data.peek())
  print(data.count)


nodes()
stacks()
