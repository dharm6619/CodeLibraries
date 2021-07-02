x, y = 10, 100

if (x<y):
    st = "x is less than y"
elif (x==y):
    st = "x is equal to y"
else:
    st = "x is greater than y"

print(st)

a, b = 3, 4
st = "a is greater than b" if (a>b) else "a is less than or equal to b"
print(st)