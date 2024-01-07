number1 = int(input("first number"))
number2 = int(input("second number"))

for m in range (1,number1*number2 +1):
    if m%number1 ==0 and m%number2 ==0:
        print("LCM of number is", m)
        break
