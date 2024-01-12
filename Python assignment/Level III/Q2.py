def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"File not found: {file_path}"

file_path = 'C:\\Users\\yashp\\OneDrive\\Desktop\\College\\Python\\Exam Practise\\Yash.txt'
lines_count = count_lines(file_path)

if isinstance(lines_count, int):
    print("This file has",lines_count,"lines.")
else:
    print(lines_count)

f=open("C:\\Users\\yashp\\OneDrive\\Desktop\\College\\Python\\Exam Practise\\Yash.txt","x")
f.write("My name is Yash")
print("Data Written Successfully")