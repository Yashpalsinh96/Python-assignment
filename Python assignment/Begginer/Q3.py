physics = 79
chemistry = 69
biology = 78
mathematics = 91
computer = 89
Total = physics + chemistry + biology + mathematics + computer
percentage = (Total / 500) * 100

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")

