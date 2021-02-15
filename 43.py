tuplex = "p", "r", "a", "k", "r", "i", "t", "i"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex)
listx.remove("p")
tuplex = tuple(listx)
print(tuplex)
