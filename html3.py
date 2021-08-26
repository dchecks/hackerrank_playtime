import re

test_data = ['<head>',
'<title>HTML</title>',
'</head>',
'<object type="application/x-flash"',
'data="your-file.swf"',
'width="0" height="0">',
'<!-- <param name="movie" value="your-file.swf" /> -->',
'<param name="quality" value="high"/>',
'</object>']

class PaserRoo:
    start_re = re.compile(r"""<.* """)
    tag_stack = []

    def open_tag(self, s):
        if s[0] == '/':
            self.end_tag()
        else:
            self.begin_tag(s)

    def begin_tag(self, s):
        tag_terminators = [' ', '/', '=']
        tag_buf = ''
        while s[0] not in tag_terminators:
            tag_buf += s[0]
            s = s[1:]




    def end_tag(self):
        self.tag_stack.pop()


    def p(self, s: str):
        s = s.lstrip()
        if s[0] == '<':
            self.open_tag(s[1:])


        if s.startswith("</"):
            pass # Close block
        elif s.startswith("<"):
            space_idx = s.find(' ')

            if space_idx >= 0:
                pass # We have attributes
            close_idx = s.find('>')
            self.end_tag()




parseroo = PaserRoo()
for s in test_data:
    parseroo.p(s)


