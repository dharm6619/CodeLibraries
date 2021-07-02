def main():
    #while loop
    x = 0
    while (x<5):
        print(x)
        x = x + 1
    #for loop 
    for x in range(5,10):
        print(x)
    # for as an iterator over objects
    days = ["Sunday", "Monday", "Tuesday"]
    for i,d in enumerate(days):
        print(i,d)
    for day in days:
        print(day)
    for x in range(5,10):
        #if (x==7): break
        if (x%2==0): continue
        print(x)


if __name__ == "__main__":
    main()
