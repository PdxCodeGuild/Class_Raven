class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.first_node = None
        self.__length = 0

    def append(self, element):
        '''Add the given element to the end of the list'''
        new_node = Node(element)
        
        # if the linked list is empty, the new node becomes the first node
        if not self.first_node:
            self.first_node = new_node

        # if the linked list has a first_node, traverse the list until the end
        else:
            current_node = self.first_node
            while current_node.next:
                current_node = current_node.next
            
            # add the new_node to the end of the list
            current_node.next = new_node
        
        # increase the list's length to include the new_node
        self.__length += 1


    def insert(self, element, index):
        '''Insert the given element at the given index'''

        # raise an IndexError if the index doesn't exist
        if index > self.__length:
            raise IndexError(f'Index out of range: {index}')

        current_node = self.first_node
        previous_node = None
        current_index = 0
        new_node = Node(element)

        # if the index is 0, the new_node becomes the first_node
        if index == 0:
            new_node.next = self.first_node
            self.first_node = new_node
        
        # otherwise, traverse the list,
        # tracking the current_node and the previous_node before it
        # until the desired index is reached,
        # add the new node at that position
        else:
            while current_node:
                if current_index == index:

                    # previous_node -> new_node -> current_node
                    previous_node.next = new_node
                    new_node.next = current_node
                    break
            
                # increase the index and progress each tracking node
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
            
            # increase the list's length to include the new_node
            self.__length += 1

    def remove(self, element):
        '''Remove the first occurrence of the given element'''

        # if the list is empty, we're done
        if not self.first_node:
            print('The list is empty')

        # if the first_node contains the given element
        # the second node becomes the first_node
        elif self.first_node.value == element:
            temp = self.first_node
            self.first_node = temp.next
            temp = None # delete the removed node from memory

            return
        else:
            # otherwise, traverse the list,
            # checking each node's next node for the target value
            current_node = self.first_node
            while current_node.next:
                # if the current_node contains the target element,
                # set the next value to the next node's next value
                if current_node.next.value == element:
                    temp = current_node.next
                    current_node.next = temp.next
                    
                    temp = None # delete the removed node from memory
                    return

                current_node = current_node.next
        
        # decrease the list's length to exclude the removed node
        self.__length -= 1

    def get(self, index):
        '''get the element at the given index (starting with 0)'''

        if index > self.__length:
            raise IndexError(f'Index out of range: {index}')

        current_node = self.first_node
        current_index = 0

        # traverse the list until the desired index
        # return the value of the node at the index
        while current_node:
            if current_index == index:
                return current_node.value

            current_index += 1
            current_node = current_node.next

    def find(self, element): # find the first occurrence of the element and return it
        current_node = self.first_node
        current_index = 0

        while current_node:
            if current_node.value == element:
                return current_index

            current_index += 1
            current_node = current_node.next

    def length(self):
        '''Return the length of the list'''
        return self.__length


    def __repr__(self):
        '''Return a string of the list's values with arrows between each'''
        current_node = self.first_node

        output = ''
        if self.__length == 0:
            output = 'The list is empty.'
        else:
            while current_node:
                output += current_node.value
                if current_node.next:
                    output += ' -> '
                current_node = current_node.next

        return output



if __name__ == '__main__':

    # instantiate a linked list
    linked_list = LinkedList()
    print(linked_list)


    # add some items, each to the end
    linked_list.append('A')
    linked_list.append('B')
    linked_list.append('C')
    linked_list.append('D')
    linked_list.append('E')

    print(linked_list.length()) # 5

    linked_list.insert('K', 0)
    print(linked_list) # K -> A -> B -> C -> D -> E

    linked_list.insert('W', 4)
    print(linked_list) # K -> A -> B -> C -> W -> D -> E
    # linked_list.insert('D', 10) # IndexError: Index out of range: 10


    linked_list.remove('C')
    print(linked_list) # K -> A -> B -> W -> D -> E


    print(linked_list.get(3)) # W
    print(linked_list.find('D')) # 4
