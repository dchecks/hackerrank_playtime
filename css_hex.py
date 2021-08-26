import re
# regex = re.compile(r"""^#$[0-9a-fA-F]{3-6}(;,\))+""")
# regex = re.compile(r"""#[0-9a-fA-F]{3,6}""")
regex = re.compile(r"""#[0-9a-fA-F]{3,6}[;,)]{1}""")

test_str = ["#BED",
"{",
"    color: #FfFdF8; background-color:#aef;",
"    font-size: 123px;",
"    background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
"}",
"#Cab",
"{",
"    background-color: #ABC;",
"    border: 2px dashed #fff;",
"}"]

for s in test_str:
    for hstr in re.findall(regex, s):
        print(hstr.strip(',);'))