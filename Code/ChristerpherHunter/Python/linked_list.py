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


def main() -> None:

    s = Stack()
    s.push(5)
    s.push(6)

    print(s.length())
    s.peek()
    print(s.pop())
    s.peek()
    print(s.pop())
    s.peek()


if __name__ == "__main__":
    main()
