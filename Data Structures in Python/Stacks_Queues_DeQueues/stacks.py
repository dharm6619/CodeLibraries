class Stack:

    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        """Accepts an item as a paramter and adds it to the end of the list. Returns none. Runtime O(1)"""
        self.items.append(item)

    def pop(self):
        """This method removes and returns the last item from the list. Runtime is O(1)"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []