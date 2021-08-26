from temp_var import h
print(h)

prim_int = 5
prim_str = "String"
prim_float = 5.5
prim_bool = True

prim_copy = prim_int
prim_int = 6

print(prim_copy)
print(prim_int)


class BananaGabi:
    def __init__(self):
        pass


b1 = BananaGabi()
b2 = b1
b2.gabrizosa = "cosas"



print("Fin")