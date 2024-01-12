text = input("string= ")

count = 0

for character in text:
    if (character in "aAeEiIoOuU"):
        count +=1

print("Number of vowels: ", count)