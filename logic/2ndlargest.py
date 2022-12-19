l = []
user_input = int(input("enter the number of entries : "))
for i in range(1,user_input+1):
    entries = int(input("enter the numbers  : "))
    l.append(entries)

l.sort()
print(l)
print("the second largest number is : ",l[-2])