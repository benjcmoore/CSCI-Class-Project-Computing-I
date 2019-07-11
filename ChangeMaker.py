print("Price of the item: ")
price = eval(input(""))
print("Cash Tendered: ")
payed = eval(input(""))

s = (payed - price)
print("Change: " + ("{0:.2f}".format(s)))
print("Change Left: " + str(int(float(str(s)) * 100)))

T = 20
t = 10
f = 5
o = 1
q = 0.25
d = 0.10
n = 0.05
p = 0.01

print("Twenties: ", s//T)
s = s%T
print("Tens: ", s//t)
s = s%t
print("Fives: ", s//f)
s = s%f
print("Ones: ", s//o)
s = s%o
print("Quarters: ", s//q)
s = s%q
print("Dimes: ", s//d)
s = s%d
print("Nickles: ", s//n)
s = s%n
print("Pennies: ", s//p)

exit()