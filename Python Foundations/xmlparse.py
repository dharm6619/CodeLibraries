import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    tag_list = doc.getElementsByTagName('book')
    print("No. of books = " + str(tag_list.length))
    for book in tag_list:
        print("Book - ", book.getAttribute("id") + " : " )
        # print(book["title"])
    new_skill = doc.createElement("book")
    new_skill.setAttribute("id", "13")
    doc.firstChild.append(new_skill)
    
if __name__=="__main__":
    main()