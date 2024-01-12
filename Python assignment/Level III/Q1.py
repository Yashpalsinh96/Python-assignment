try:
    with open('path/to/doc.txt', 'r') as file:
        content = file.read()

        words = content.split()

        even_length_strings = [word for word in words if len(word) % 2 == 0]

        result = ' '.join(even_length_strings)

        print(result)

except FileNotFoundError:
    print("File not found.")
