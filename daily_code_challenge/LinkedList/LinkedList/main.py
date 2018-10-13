class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.top = None

    def add(self, data):
        if self.top == None:
            self.top = Node(data, None)
            self.last = self.top
        else:
            node = Node(data, None)
            last = self.get_last()
            last.next_node = node

    def size(self):
        result = 0
        node = self.top
        while node != None:
            result += 1
            node = node.next_node
        return result;

    def get_last(self):
        last = self.top
        while last.next_node != None:
            last = last.next_node
        return last

    def insert(self, index, data):
        if self.size() > index:
            previous_node = self.top
            for x in range(0, index-1):
                previous_node = previous_node.next_node

            new_node = Node(data, None)
            if previous_node == self.top: 
                # special case when top is the only node
                new_node.next_node = self.top
                self.top = new_node
            else:
                new_node.next_node = previous_node.next_node
                previous_node.next_node = new_node

    def to_array(self):
        result = []
        node = self.top
        while node != None:
            result.append(node.data)
            node = node.next_node
        return result;





if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(4)
    linked_list.add(8)
    linked_list.add(6)
    print(f"{linked_list.to_array()}")

