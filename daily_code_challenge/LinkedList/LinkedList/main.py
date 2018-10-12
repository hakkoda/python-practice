class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.top = None

    def.add(self, data):
        if self.top == None:
            self.top = Node(data, None)

    def display(self):
        pass




if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(4)
    linked_list.add(8)
    linked_list.add(6)
    linked_list.display()

