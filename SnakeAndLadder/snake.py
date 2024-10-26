class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __eq__(self, other):
        return self.head == other.head and self.tail == other.tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
