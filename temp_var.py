h = 5
class GUnit:
    i = 6
    def __init__(self, cuanto):
        self.cuanto = cuanto
        j = 7
        self.k = 8




units = []

c = 88
while True:
    print("%s: %s" % (c, GUnit(c).cuanto))
    c += 1

print("Fin")