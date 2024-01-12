my_list = [0,1,2,3,4,5,6,7]

try:
    index = int(input("Enter the index to access: "))
    result = my_list[index]
    print("Value at index {index}: {result}")

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Please enter a valid integer for the index")
