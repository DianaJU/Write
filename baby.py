n = float(input("A number: "))
def baby(n):
    og = -1
    g = 1
    while abs(g - og) > 1:
        og = g
        g = (g + n/g) / 2
    return g
print(baby(n))
