import urllib.request
import json

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print(weburl.getcode())
    data = weburl.read()
    print(data)

if __name__=="__main__":
    main()