class Sand:
    pass

class Beach:
    def __init__(self):
        self.open = False

    def weGot(self):
        return "Sand"
#main method

b = Beach()
print(b.weGot())
b.open = False
