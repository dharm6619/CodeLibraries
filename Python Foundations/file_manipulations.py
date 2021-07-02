def main():
    #Create a file 
    # f = open("sample.txt", "w+")
    # for i in range(10):
    #     f.write("This is line " + str(i)+"\n")
    # f.close()
    # f = open("sample.txt", "a")
    # for i in range(10):
    #     f.write("This is new line " + str(i)+"\n")
    # f.close()
    f = open("sample.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for lines in fl:
            print(lines)


    

if __name__ == "__main__":
    main()
