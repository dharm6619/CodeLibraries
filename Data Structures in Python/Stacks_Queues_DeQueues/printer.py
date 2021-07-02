from random import randint

class PrintQueue():
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


class Job:
    def __init__(self) -> None:
        self.pages = randint(0, 10)
    
    def print_page(self):
        print(self.pages)
        self.pages = self.pages -1
    
    def check_complete(self):
        if self.pages == 0:
            return True
        else:
            return False


class Printer:
    def __init__(self) -> None:
        self.current_job = None
    
    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No More Jobs To Print"
    
    def print_job(self, job):
        while job.pages>0:
            job.print_page()
        if job.check_complete():
            return "Printing Complete"
        else:
            return "ERROR DURING PRINT"
        