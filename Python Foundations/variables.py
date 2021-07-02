# Declaration of a variable 

f=0
print(f)

f="abc"
print(f)

# print("abc " * 2)

# print("abc " + str(123))

def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

del f
print(f)

