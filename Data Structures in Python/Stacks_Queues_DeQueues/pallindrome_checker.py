from deque import Deque


def is_pallindrome(x):
    my_d = Deque()
    for letter in x:
        my_d.add_rear(letter)
    while not my_d.is_empty():
        if my_d.peek_front() != my_d.peek_rear():
            return False
        my_d.remove_front()
        my_d.remove_rear()
    return True
    

def main():
    x = input("Enter the String to Check: ")
    print("Valid: ",is_pallindrome(x))

if __name__ == "__main__":
    main()
