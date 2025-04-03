def insert_at_begining(self, date):
    new_node = Node(date)
    if self.head:
        new_node.next = self.head
    else:
        self.head = new_node
        self.tail = new_node