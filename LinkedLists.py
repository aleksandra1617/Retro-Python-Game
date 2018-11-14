class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def add_last(self, node):

        new_node = node

        if self.head is None:

            self.head = new_node
            self.tail = new_node
            self.size += 1

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
            self.size += 1

    def add_first(self, node):

        new_node = node

        if self.head is None:

            self.head = new_node
            self.tail = new_node

            self.size += 1

        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node

            self.head = new_node

            self.size += 1

    def delete_last(self):
        self.size -= 1

        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def get_at_pos(self, pos):
        count = 0
        curr_node = self.head

        while curr_node is not None:
            if count != pos:

                # Fetch the next node
                curr_node = curr_node.next
                count += 1

            else:
                return curr_node

        print("The specified position is invalid! Could not find Node. ")
        return None
