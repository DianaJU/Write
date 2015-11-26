def naturalpalindromes(i):
    i = str(i)
    i = i[::-1]
    i = int(i)
    return i
lower = int(input("Lower bound of the sequence: "))
upper = int(input("Upper bound of the sequence: "))
x = []
p = 0
n = 0
c = 0
l = 0
for h in range(upper-lower+1):
    x.append(l)
    l = l + 1
if(upper<lower):
    print("Please check your numbers and try again.")
else:
    for i in x:
        i = i + 1
        x = naturalpalindromes(i)
        if (x == i):
            p = p + 1
        else:
            non1 = x + i
            non2 = naturalpalindromes(non1)
            for z in range(30):
                if non1 == non2:
                    n = n + 1
                    break
                else:
                    non1 = non1 + non2
                    non2 = naturalpalindromes(non1)
                if(z == 29):
                    c = c + 1
    print("Range of numbers analysed: "+ str(lower) + "to" + str(upper))
    print("Number of natural palindromes : " + str(p))
    print("Number of non-Lychrels encountered: " + str(n))
    print("Number of Lychrel candidates: " + str(c))
