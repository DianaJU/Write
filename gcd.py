a = int(input("First integer: "))
b = int(input("Second integer: "))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)
print(gcd(a,b))
