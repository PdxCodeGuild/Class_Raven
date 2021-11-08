"""
Christerpher Hunter
Optional Lab: Linked List

A stack is a FILO (first-in, last-out) data structure that can be visualized
like a stack of plates. The only accessible item is the 'top'. There are three
operations that can be performed.

push: add a new item to the top of the stack, the previous top item goes
underneath it.
pop: removes the item from the top of the stack and returns it, the one below
it becomes the new top item.
peek: returns the item at the top of the stack without modifying anything.
"""


class Stack:
    """FILO (First in Last out) stack"""

    def __init__(self) -> None:

        self.top = list()

    def push(self, element):
        """insert an element at the start (new root)"""

        self.top.append(element)

    def pop(self) -> int:
        """remove an element from the start (the root becomes the next node)"""

        return self.top.pop()

    def peek(self) -> int:
        """returns the item at the top of the stack without modification"""

        print(f"{self.top}")

    def length(self) -> int:
        """return the number of elements"""

        return len(self.top)

    def __str__(self):
        return f"({self.top})"


class LinkedList:
    """an implementation of a Linked List"""

    def __init__(self):
        self.root = []

    def append(self, element):
        """add the element to the end"""

        self.root.append(element)

    def insert(self, element, index):
        """insert the element at the given index"""

        self.root.insert(index, element)

    def remove(self, element):
        """remove the first occurrence of the element"""

        self.root.remove(element)

    def get(self, index):
        """get the element at the given index (starting with 0)"""

        return self.root.pop(index)

    def find(self, element):
        """find the first occurrence of the element and return it"""

        for i in self.root:
            if i == element:
                return i

    def length(self):
        """return the length of the list"""

        return len(self.root)

    def __str__(self) -> str:
        return(f"{self.root}")


def main() -> None:

    print("\nStack")
    s = Stack()
    s.push(5)
    s.push(6)

    print(s.length())
    s.peek()
    print(s.pop())
    s.peek()
    print(s.pop())
    s.peek()

    print("\n")
    print("LinkedList")

    nums = LinkedList()
    nums.append(5)
    nums.append(6)
    nums.insert(7, 0)
    print(nums)  # [7, 5, 6]
    print(nums.find(5))  # 1
    nums.remove(5)
    print(nums)  # [7, 6]
    print(nums.length())  # 2


if __name__ == "__main__":
    main()
