def func1():
    print("I am a function")

# Function with args
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#Function with return value
def cube(x):
    return x*x*x

#Function with a default value for argument
def power(num, x=1):
    result = 1
    for i in range(x):
        i = i
        result = result * num
    return result

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func2(10,20)
print(func2(10,20))
print(cube(3))

print(power(3))
print(power(4,2))
print(power(x=4,num = 3))
print(multi_add(4,5))
print(multi_add(4,5,6,7,8,9))
