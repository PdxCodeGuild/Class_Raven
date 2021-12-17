class node:
  def __init__(node, item, next=None):
    node.item = item
    node.next = next

  def __str__(node):
    return f'({node.item}, {node.next})'
