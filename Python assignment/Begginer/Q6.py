num = int(input("Enter the number:"))
result = 0
for i in range(1,num):
    if (num%i) == 0:
        result = result+i
if result == num:
    print(num, "Perfect Number")
else:
    print(num, "Not a perfect number")

