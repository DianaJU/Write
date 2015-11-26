data = open("93cars.dat.txt","r")
gmc = 0
gmh = 0
mrp = 0
cars = 0
f = 1
for x in data:
    if f % 2 == 1:
        gmc = gmc + float(x[52:54])
        gmh = gmh + float(x[55:57])
        mrp = mrp + float(x[42:46])
        cars = cars + 1
    f = f + 1
x = round(gmc/cars)
y = round(gmh/cars)
z = round(mrp/cars)

print("Average gas mileage in city: " + str(x))
print("Average gas mileage on highway: " + str(y))
print("Average midrange price of the vehicles: " + str(z))
