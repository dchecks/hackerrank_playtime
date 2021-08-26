# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def handle_attrs(self, attrs):
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attrs(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attrs(attrs)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
sb = ""

istr = ["<html><head><title>HTML Parser - I</title></head>",
"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"]

for i in istr:
    sb += i

parser.feed(sb)