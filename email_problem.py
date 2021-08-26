import email.utils as ue
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils as eu


def parse(address):
    valid_nonalpha = ['-', '.', '_']

    if not len(address):
        return False

    if not address[0].isalpha():
        return False

    at_split = address.split('@')
    if len(at_split) != 2:
        return False

    for c in at_split[0]:
        if not c.isalnum() and c not in valid_nonalpha:
            return False

    dot_split = at_split[-1].split('.')
    if len(dot_split) != 2:
        return False

    if not ''.join(dot_split).isalpha():
        return False

    if not (0 < len(dot_split[-1]) <= 3):
        return False

    return True


# es = ["dheeraj <dheeraj-234@gmail.com>",
# "crap <itsallcrap>",
# "harsh <harsh_1234@rediff.in>",
# "kumal <kunal_shin@iop.az>",
# "mattp <matt23@@india.in>",
# "harsh <.harsh_1234@rediff.in>",
# "harsh <-harsh_1234@rediff.in>"]
# e = eu.parseaddr("DEXTER <dexter@hotmail.com>")
# e = eu.parseaddr("VIRUS <virus!@variable.:p>")
es = ["vin <vineet@>",
"vineet <vineet@gma.il.co.m>",
"vineet <vineet@gma-il.co-m>",
"vineet <vineet@gma,il.co@m>",
"vineet <vineet@gmail,com>",
"vineet <.vin@gmail.com>"]
for e1 in es:
    e = eu.parseaddr(e1)
    success = parse(e[-1])
    print(success, e1, ue.formataddr(e))

