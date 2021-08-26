from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment ")
        print(data)

    def handle_data(self, data):
        if not data == "\n":
            print(">>> Data\n%s" % data)


html = ""
html += "<!--[if IE 9]>IE9-specific content\n"
html += "<![endif]-->\n"
html += "<div> Welcome to HackerRank</div>\n"
html += "<!--[if IE 9]>IE9-specific content<![endif]-->\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()