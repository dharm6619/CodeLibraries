class MyClass():
    def method1(self):
        print("My Class Method")
    
    def method2(self, somestring):
        print(" Hi there !!! ", somestring)

class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("My AnotherClass Method")
    
    def method2(self):
        print(" Hi there !!! From another class")

def main():
    c = MyClass()
    c.method1()
    c.method2("Dharmendra")
    c2 = AnotherClass()
    c2.method1()
    c2.method2()

if __name__ == "__main__":
    main()