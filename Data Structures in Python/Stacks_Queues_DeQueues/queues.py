class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        """Inserts an item to the front of the list. Runtime is O(n)"""
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]

    def is_empty(self):
        return self.items == []
    