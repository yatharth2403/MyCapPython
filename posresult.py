list1 = []
len = int(input("Enter the length of the list: "))
print("Enter the numbers: ")
for i in range(len):
    val = int(input())
    list1.append(val)
print("The list you entered is: ", list1)
j = 0
while j < len:
    if list1[j] >= 0:
        print(list1[j])
    j += 1
