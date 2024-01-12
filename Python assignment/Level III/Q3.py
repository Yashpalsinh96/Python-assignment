def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        corrected_content = content.replace('J', 'I').replace('j', 'i')
        
        with open(file_path, 'w') as file:
            file.write(corrected_content)
        
        print(f"Corrections made and saved to {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

new_file_path = 'C:\\Users\\yashp\\OneDrive\\Desktop\\College\\Python\\Exam Practise\\Q3.txt'
with open(new_file_path, 'w') as f:
    f.write("My name is Joker")
print("Data Written Successfully")

JtoI(new_file_path)