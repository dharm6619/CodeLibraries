class Deque:

    def __init__(self) -> None:
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items == []:
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.items == []:
            return None
        return self.items.pop()

    def peek_front(self):
        if self.items == []:
            return None
        return self.items[0]

    def peek_rear(self):
        if self.items == []:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []