input_sentence = "Hello, World! Welcome to python programming."
words = input_sentence.split(" ")

words = words[-1::-1]
output =' '.join(words)
print("output after reverse = ", output)