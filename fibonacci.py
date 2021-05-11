lim = int(input("Enter the number of elements you want to print: "))
i = 1
x = 0
y = 1
z = 0
print("Your fibonacci series: ")
while i <= lim:
    print(z)
    x = y
    y = z
    z = x+y
    i += 1
