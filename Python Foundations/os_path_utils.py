import os 
from os import path
from datetime import date,time,datetime,timedelta
import time

def main():
    print(os.name)
    #Check the existence of a file 
    print(path.exists("sample.txt"))
    print(path.isfile("sample.txt"))
    print(path.isdir("sample.txt"))
    print(path.realpath("sample.txt"))
    print("Path and real path",path.split(path.realpath("sample.txt")))
    print("File modification time : ", path.getmtime("sample.txt"))
    print("File modification time : ", datetime.fromtimestamp(path.getmtime("sample.txt")))
    mtime = datetime.fromtimestamp(path.getmtime("sample.txt"))
    td = datetime.now()
    print("It has been "+ str(td-mtime) + " since it has been modified which is " + str((td-mtime).total_seconds()) + " seconds")


if __name__ == "__main__":
    main()