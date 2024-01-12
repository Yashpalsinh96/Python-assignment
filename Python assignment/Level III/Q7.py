students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

result_dict = {}
for i in range(len(students)):
    result_dict[students[i]] = subjects[i]

print(result_dict)
# --------------------------------------------
# students = ["Sam", "Alice", "Mona"]
# subjects = ["Commerce", "Science", "Computer"]

# result_dict = {students[i]: subjects[i] for i in range(len(students))}

# print(result_dict)