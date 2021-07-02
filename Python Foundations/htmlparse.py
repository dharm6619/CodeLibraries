from html.parser import HTMLParser

metacount=0
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered Comment : ", data)
        pos = self.getpos()
        print("\t at Line: ",pos[0]," Position: ", pos[1])
    
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag=='meta':
            metacount += 1
        print("Encountered Tag : ", tag)
        pos = self.getpos()
        print("\t at Line: ",pos[0]," Position: ", pos[1])
        if attrs.__len__()>0:
            for a in attrs:
                print("\t Attr: ", a[0], " = ", a[1])

        

    def handle_endtag(self, tag):
        print("Encountered Endtag : ", tag)
        pos = self.getpos()
        print("\t at Line: ",pos[0]," Position: ", pos[1])

    def handle_data(self,data):
        if(data.isspace()):
            return
        print("Encountered Data : ", data)
        pos = self.getpos()
        print("\t at Line: ",pos[0]," Position: ", pos[1])
    


def main():
    myParser = MyHTMLParser()
    f = open("sample_html.html")
    if f.mode=="r":
        contents = f.read()
        myParser.feed(contents)
    print("Meta tags count: " + str(metacount))


if __name__=="__main__":
    main()