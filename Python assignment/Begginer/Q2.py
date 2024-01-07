input_string = input("Enter a string")

Number_of_digits = 0
Letters = 0

for char in input_string:
    if char.isalpha():
        Letters += 1
    elif char.isdigit():
        Number_of_digits +=1

print("Alphabets: ", Letters)
print("Number: ", Number_of_digits)

