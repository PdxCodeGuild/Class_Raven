class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class Stack:
    def __init__(self):
        self.top_node = None
        self.__height = 0

    def push(self, element):
        '''insert an element at the start (new top_node)'''
        new_node = Node(element)

        # if there is no current top to the stack
        if not self.top_node:
            self.top_node = new_node
        
        # otherwise the new_node becomes the top_node
        else:
            new_node.next = self.top_node
            self.top_node = new_node

        # indicate the height has increased
        self.__height += 1

    def pop(self): 
        '''remove an element from the start (the top_node becomes the next node)'''
        # raise an error if the stack is empty
        if self.__height == 0:
            raise IndexError('Pop from empty stack.')

        temp = self.top_node
        self.top_node = temp.next
        temp = None

        # decrease the height because a node got removed
        self.__height -= 1

    def peek(self): 
        ''' returns the top_node or None if there is no top_node'''
        return self.top_node

    @property # decorator to allow the height to be accessed like an attribute of the class
    def height(self):
        '''return the number of elements in the stack'''
        return self.__height

    def __str__(self):
        if self.__height == 0:
            output = 'The stack is empty.'

        else:
            output = ''
            current_node = self.top_node

            while current_node:
                output += current_node.value + '\n'
                current_node = current_node.next

        return output


if __name__ == '__main__':
    stack = Stack() # instatiate a stack
    # print(stack.height)
    # stack.pop() # IndexError: Pop from empty stack.



    stack.push('C')
    # print(stack)
    # print(stack.height) # 1

    stack.push('B')
    # print(stack)
    # print(stack.height) # 2

    stack.push('A')
    # print(stack)
    # print(stack.height) # 3


    # print(stack.peek()) # A
    stack.pop()
    print(stack)
    print(stack.height) # 2
