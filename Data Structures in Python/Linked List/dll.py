class DLLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self) -> str:
        return "DLL NODE: data = {}".format(self.data)
    
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
    
    def get_previous(self):
        """Return self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Set the self.previous value to new_previous"""
        self.previous = new_previous
