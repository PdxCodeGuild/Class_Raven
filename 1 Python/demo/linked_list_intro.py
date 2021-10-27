class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

n1 = Node(5)

print(n1)
print(n1.next)

n2 = Node(3)
n1.next = n2 # link n1 to n2

print(n1.next)
