class SLLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return "SLL NODE: data = {}".format(self.data)
    
    def get_data(self):
        """ Return Data values"""
        return self.data

    def set_data(self, new_data):
        """ Replace the data value with new data"""
        self.data = new_data

    def get_next(self):
        """Return self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Set the self.next value to new_next"""
        self.next = new_next

class SLL:

    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        return "SLL Object: Data {}".format(self.head)
    
    def is_empty(self):
        """Returns True if list is empty else False"""
        return self.head is None

    def add_front(self, new_data):
        """Adds a Node with new_data to the front of the Linked List"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Returns the size of the Linked List"""
        counter = 0
        if self.is_empty():
            return 0
        else:
            current = self.head
            while current is not None:
                counter = counter + 1
                current = current.get_next()
        return counter

    def search(self, data):
        """Returns True if the data is found else false"""
        result = False
        current = self.head
        while current is not None:
            if current.get_data() == data:
                result = True
                break
            current = current.get_next()
        return result
        
    def remove(self, data):
        """Remove the first occurrence of the node if data is found.."""
        if self.is_empty() or not self.search(data):
            print("Either List is empty or Node with data not found")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current.get_data() == data:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            
    
    def print_list(self):
        """Prints The Linked List"""
        if self.is_empty():
            print("Empty List")
            return []
        else:
            current = self.head
            data = []
            while current is not None:
                data.append(current.get_data())
                current = current.get_next()
            return data
            

    

