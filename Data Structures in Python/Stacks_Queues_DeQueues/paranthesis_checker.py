from stacks import Stack


def is_valid(x):
    my_stack = Stack()
    for s in x:
        if s in ['(', '{', '[']:
            my_stack.push(s)
        elif s == ')' and my_stack.peek() == '(':
            my_stack.pop()
        elif s == '}' and my_stack.peek() == '{':
            my_stack.pop()
        elif s == ']' and my_stack.peek() == '[':
            my_stack.pop()
        else:
            my_stack.push(s)
    return my_stack.isEmpty()


def main():
    x = input("Enter the String to Check: ")
    print("Valid: ",is_valid(x))

if __name__ == "__main__":
    main()
